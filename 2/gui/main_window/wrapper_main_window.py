from gui.main_widget import Main_widget
from gui.main_window.main_window import Ui_MainWindow


from PySide2.QtWidgets import QMainWindow


class Main_window(QMainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.main_widget = Main_widget(self)
        self.setGeometry(self.main_widget.geometry())
        self.setCentralWidget(self.main_widget)
        self.show()

