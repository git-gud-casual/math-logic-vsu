from PySide6.QtCore import Signal, QThread
import matrix_funcs
from typing import List, Optional


class MatrixCalculateQThread(QThread):
    matrix: Optional[List[List[int]]] = None
    result_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def set_matrix(self, matrix: List[List[int]]):
        self.matrix = matrix

    def run(self):
        assert self.matrix is not None
        result = self.get_answers()
        self.result_signal.emit(result)

    def get_answers(self):
        try:
            solves = self.calculate(self.matrix)
            if isinstance(solves, list):
                return self.get_pretty_solves(solves)
            else:
                return "System of linear equations has infinity solves"
        except ZeroDivisionError:
            return "System of linear equations has not any solves"

    @staticmethod
    def get_pretty_solves(solves: List[float]):
        s = ""
        for i, x in enumerate(solves):
            s += f"x{i + 1}={x}\n"
        return s

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
