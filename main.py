import sys
from PySide6 import QtWidgets

from windows import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
