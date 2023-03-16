#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdint.h>
#include <stdio.h>

int64_t get_matrix_determinant(size_t rows, size_t columns, int64_t matrix[rows][columns]) {
    if (rows <= 1 && columns <= 1) {
        return matrix[0][0];
    }

    int64_t det = 0;
    for (size_t i = 0; i < columns; i++) {
        // Get minor
        int64_t minor[rows - 1][columns - 1];
        for (size_t y = 1; y < rows; y++) {
            for (size_t x = 0; x < columns; x++) {
                if (i != x && y != 0) {
                    minor[y - 1][x - (x < i ? 0 : 1)] = matrix[y][x];
                }
            }
        }

        det += matrix[0][i] * (i % 2 == 0 ? 1 : -1) * get_matrix_determinant(rows - 1, columns - 1, minor);
    }
    return det;
}

static PyObject *matrix_determinant(PyObject *self, PyObject *args) {
    PyObject *list;
    int64_t result;

    uint8_t first_iteration_flag = 1;
    size_t matrix_rows, matrix_columns, sublist_length;
    int64_t **matrix;

    if (!PyArg_ParseTuple(args, "O", &list)) {
        return NULL;
    }
    list = PySequence_Fast(list, "argument must be iterable");
    if (list == NULL) {
        return NULL;
    }
    
    matrix_rows = PySequence_Fast_GET_SIZE(list);
    for (size_t i = 0; i < matrix_rows; i++) {
        PyObject *sublist;
        sublist = PySequence_Fast_GET_ITEM(list, i);
        if (sublist == NULL) {
            if (!first_iteration_flag) {
                for (size_t row = 0; row < matrix_rows; row++) {
                    free(matrix[row]);
                }
                free(matrix);
            }
            Py_DECREF(list);
            return NULL;
        }
        sublist = PySequence_Fast(sublist, "all items must be iterable");
        if (sublist == NULL) {
            if (!first_iteration_flag) {
                for (size_t row = 0; row < matrix_rows; row++) {
                    free(matrix[row]);
                }
                free(matrix);
            }
            Py_DECREF(list);
            return NULL;
        }

        sublist_length = PySequence_Fast_GET_SIZE(sublist);
        if (!first_iteration_flag) {
            if (sublist_length != matrix_columns || matrix_columns != matrix_rows) {
                Py_DECREF(list);
                Py_DECREF(sublist);
                PyErr_SetString(PyExc_ValueError, "list must be square");
                for (size_t row = 0; row < matrix_rows; row++) {
                    free(matrix[row]);
                }
                free(matrix);
                return NULL;
            }
        }
        else {
            matrix_columns = sublist_length;
            matrix = malloc(sizeof(int64_t*) * matrix_rows);
            if (matrix == NULL) {
                Py_DECREF(list);
                Py_DECREF(sublist);
                return PyErr_NoMemory();
            }
            for (size_t row = 0; row < matrix_rows; row++) {
                matrix[row] = malloc(sizeof(int64_t) * matrix_columns);
                if (matrix[row] == NULL) {
                    Py_DECREF(list);
                    Py_DECREF(sublist);
                    return PyErr_NoMemory();
                }
            }
            first_iteration_flag = 0;
        }

        for (size_t j = 0; j < matrix_columns; j++) {
            PyObject *item = PySequence_Fast_GET_ITEM(sublist, j);
            if (item == NULL) {
                Py_DECREF(list);
                Py_DECREF(sublist);
                for (size_t row = 0; row < matrix_rows; row++) {
                    free(matrix[row]);
                }
                free(matrix);
                return NULL;
            }
            item = PyNumber_Long(item);
            if (item == NULL) {
                Py_DECREF(list);
                Py_DECREF(sublist);
                for (size_t row = 0; row < matrix_rows; row++) {
                    free(matrix[row]);
                }
                free(matrix);
                PyErr_SetString(PyExc_TypeError, "all items of sublist must be numbers");
                return NULL;
            }

            matrix[i][j] = PyLong_AS_LONG(item);
            Py_DECREF(item);
        }
        Py_DECREF(sublist);
    }

    Py_DECREF(list);
    int64_t matrix_array[matrix_rows][matrix_columns];
    for (size_t i = 0; i < matrix_rows; i++) {
        for (size_t j = 0; j < matrix_columns; j++) {
            matrix_array[i][j] = matrix[i][j];
        }
        free(matrix[i]);
    }
    free(matrix);
    result = get_matrix_determinant(matrix_rows, matrix_columns, matrix_array);
    return Py_BuildValue("l", result);
}

static PyMethodDef determinantMethods[] = {
    {"determinant", matrix_determinant, METH_VARARGS, "Get determinant of matrix."},
    {0} /* sentinel */
};

static struct PyModuleDef matrixModule = {
    PyModuleDef_HEAD_INIT,
    "matrix_funcs",
    "Python interface for the determinant C function",
    -1,
    determinantMethods
};

PyMODINIT_FUNC PyInit_matrix() {
    return PyModule_Create(&matrixModule);
}