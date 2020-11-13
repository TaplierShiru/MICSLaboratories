from gui.main_window.main_window import Ui_MainWindow
from gui.main_widget import Main_widget
from PySide2.QtWidgets import QMainWindow, QDesktopWidget


class Main_window(QMainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.main_widget = Main_widget(self)
        self.setCentralWidget(self.main_widget)
        self.resize(800, 600)
        self.center()
        self.setWindowTitle("Main window")
        self.show()

    def center(self):
        """
        Centers the window on the screen

        """

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            int((screen.width() - size.width()) / 2),
            int((screen.height() - size.height()) / 2)
        )

