from gui import MainWindow

from PySide2.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)

    _ = MainWindow()

    sys.exit(app.exec_())
