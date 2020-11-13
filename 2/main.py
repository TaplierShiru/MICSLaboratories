
from PySide2.QtWidgets import QApplication
import sys
from gui import Main_window


def main():
    app = QApplication(sys.argv)

    _ = Main_window()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

