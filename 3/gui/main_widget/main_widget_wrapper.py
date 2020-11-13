from gui.main_widget.main_widget import Ui_Form
from PySide2.QtWidgets import QWidget


class Main_widget(QWidget):
    def __init__(self, parent):
        super(Main_widget, self).__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setLayout(self.ui.gridLayout)

        self.__setup_buttons()

    def __setup_buttons(self):
        self.ui.pushButton_start_game.clicked.connect(self.ui.frame_game_shower.start_game)
        self.ui.pushButton_start_game.clicked.connect(self.__refresh_text_box)

    def __refresh_text_box(self):
        self.ui.plainTextEdit_game_info.clear()

