import sys

from PySide6 import QtCore, QtWidgets

from ui.Ui_MainWindow import Ui_MainWindow

from os import getcwd

from typing import List, Optional


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
                self.ui.answersPlainText.setPlainText("Error: matrix has wrong format")
            self.calculate(matrix)

    @staticmethod
    def calculate(matrix: List[List[int]]) -> Optional[List[int]]:
        pass

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
                        self.ui.answersPlainText.setPlainText("Error: matrix has wrong format")
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
