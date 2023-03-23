from PySide6 import QtCore, QtWidgets
from os import getcwd
from typing import List, Optional

from ui import Ui_MainWindow
import matrix_funcs


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addLineBtn.clicked.connect(self.add_line)
        self.ui.deleteLineBtn.clicked.connect(self.del_line)
        self.ui.loadFromFileBtn.clicked.connect(self.load_matrix_from_file)
        self.ui.getAnswersBtn.clicked.connect(self.get_answers)

    @QtCore.Slot()
    def get_answers(self):
        matrix = self.get_matrix_from_table()
        if matrix:
            if not self.is_correct_matrix(matrix):
                self.ui.answersPlainText.setPlainText("Error: matrix_funcs has wrong format")
            try:
                solves = self.calculate(matrix)
                if isinstance(solves, list):
                    self.ui.answersPlainText.setPlainText(", ".join(map(str, solves)))
                else:
                    self.ui.answersPlainText.setPlainText("System of linear equations has infinity solves")
            except ZeroDivisionError:
                self.ui.answersPlainText.setPlainText("System of linear equations has not any "
                                                      "solves")

    @staticmethod
    def calculate(matrix: List[List[int]]) -> Optional[List[float] | float]:
        reversed_matrix = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(reversed_matrix) <= j:
                    reversed_matrix.append([])
                reversed_matrix[j].append(matrix[i][j])

        solves = []
        delta0 = matrix_funcs.determinant(reversed_matrix[:-1])
        has_inf_solves = delta0 == 0
        for i in range(len(reversed_matrix) - 1):
            temp = reversed_matrix[i]
            reversed_matrix[i] = reversed_matrix[-1]
            delta = matrix_funcs.determinant(reversed_matrix[:-1])

            has_inf_solves = has_inf_solves and delta == 0
            if not has_inf_solves:
                solves.append(delta / delta0)
            reversed_matrix[i] = temp
        if has_inf_solves:
            return float("inf")
        return solves

    @QtCore.Slot()
    def load_matrix_from_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,
                                                         'Open file',
                                                         getcwd(), 'Text Files (*.txt)')[0]
        if filename:
            with open(filename) as f:
                try:
                    matrix = self.get_matrix_from_file(f)
                    if not self.is_correct_matrix(matrix):
                        self.ui.answersPlainText.setPlainText("Error: matrix_funcs has wrong format")
                        return
                    self.set_table_by_matrix(matrix)
                except ValueError:
                    self.ui.answersPlainText.setPlainText("Error: wrong number format")

    def get_matrix_from_table(self) -> Optional[List[List[int]]]:
        matrix = []
        try:
            for i in range(self.ui.coeffTable.rowCount()):
                matrix.append([])
                for j in range(self.ui.coeffTable.columnCount()):
                    matrix[i].append(int(self.ui.coeffTable.item(i, j).text()))
                matrix[i].append(int(self.ui.freeCoeffTable.item(i, 0).text()))
            return matrix
        except (ValueError, AttributeError) as e:
            if isinstance(e, ValueError):
                self.ui.answersPlainText.setPlainText("Error: wrong number format")
            else:
                self.ui.answersPlainText.setPlainText("Error: table filling is not complete")

    def set_table_by_matrix(self, matrix: List[List[int]]):
        self.ui.coeffTable.setRowCount(len(matrix))
        self.ui.freeCoeffTable.setRowCount(len(matrix))
        if len(matrix) > 0:
            self.ui.coeffTable.setColumnCount(len(matrix[0]))

        for i, line in enumerate(matrix):
            for j, val in enumerate(line):
                item = QtWidgets.QTableWidgetItem(str(val))
                if j < len(line) - 1:
                    self.ui.coeffTable.setItem(i, j, item)
                else:
                    self.ui.freeCoeffTable.setItem(i, 0, item)

    @QtCore.Slot()
    def add_line(self):
        self.ui.coeffTable.setColumnCount(self.ui.coeffTable.columnCount() + 1)
        self.ui.coeffTable.setRowCount(self.ui.coeffTable.rowCount() + 1)

        self.ui.freeCoeffTable.setRowCount(self.ui.freeCoeffTable.rowCount() + 1)

    @QtCore.Slot()
    def del_line(self):
        if self.ui.coeffTable.columnCount() > 0:
            self.ui.coeffTable.setColumnCount(self.ui.coeffTable.columnCount() - 1)
            self.ui.coeffTable.setRowCount(self.ui.coeffTable.rowCount() - 1)

            self.ui.freeCoeffTable.setRowCount(self.ui.freeCoeffTable.rowCount() - 1)

    @staticmethod
    def is_correct_matrix(matrix: List[List[int]]):
        return len(matrix) == 0 or (len(matrix) + 1 == len(matrix[0]))

    @staticmethod
    def get_matrix_from_file(file) -> List[List[int]]:
        matrix = []
        for line in file:
            matrix.append(list(map(int, line.split())))
        return matrix
