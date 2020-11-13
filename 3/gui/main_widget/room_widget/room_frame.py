from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QFrame
from PySide2.QtGui import QPaintEvent, QPainter, QPen, Qt

from gui.main_widget.room_widget.frame_logic.game_controller import GameController
from gui.main_widget.room_widget.signals.data_sender import DataSender
from logic.gun_utils.gun_txt_info import TEXT_DATA


class QRoomFrame(QFrame):

    def __init__(self, parent, speed=20):
        super(QRoomFrame, self).__init__(parent)
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(parent.update)
        signal_data_sender = DataSender()
        signal_data_sender.game_finished.connect(self.__reset_all_stuf)

        signal_data_sender.send_lucky.connect(
            lambda x: parent.parent().ui.lineEdit_cur_lucky.setText(str(x))
        )
        signal_data_sender.send_brain_strength.connect(
            lambda x: parent.parent().ui.lineEdit_cur_brain.setText(str(x))
        )
        signal_data_sender.send_remain_time.connect(
            lambda x: parent.parent().ui.lcdNumber_timecount.display(x)
        )
        signal_data_sender.send_cur_state.connect(
            lambda x: parent.parent().ui.plainTextEdit_game_info.setPlainText(
                 parent.parent().ui.plainTextEdit_game_info.toPlainText() + '\n' + TEXT_DATA[x]
            )

        )
        signal_data_sender.game_finished_info.connect(
            lambda x: parent.parent().ui.plainTextEdit_game_info.setPlainText(
                 parent.parent().ui.plainTextEdit_game_info.toPlainText() + '\n' + x
            )

        )

        self._game_controller = GameController(signal_data_sender)
        self.__timer_game = QTimer(self)
        self.__timer_game.timeout.connect(self.__control_step)

        self.__timer_afk = QTimer(self)
        self.__timer_afk.timeout.connect(self.__reset_game_timer)
        self.__timer_afk.setSingleShot(True)

        self.__speed = speed
        self.__is_game_ended = False
        self._were_afk = False

    def __control_step(self):
        if not self._were_afk and not self.__is_game_ended:
            self.__timer_game.stop()
            self._were_afk = True
            self.__timer_afk.start(self.__speed * 20)
        elif self._were_afk:
            self._were_afk = self._game_controller.take_a_step()

    def start_game(self):
        self._game_controller = GameController(self._game_controller.get_data_sender())
        self.__timer.start(self.__speed)
        self.__timer_game.start(int(self.__speed * 1.5))
        self._were_afk = False
        self.__is_game_ended = False

    def __reset_game_timer(self):
        self.__timer_game.start(int(self.__speed*1.5))

    def __reset_all_stuf(self):
        if self.__timer_afk.isActive():
            self.__timer_afk.stop()
        self.__timer_game.stop()
        self.__is_game_ended = True

    def paintEvent(self, arg__1: QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp: QPainter):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        # Draw player
        self._game_controller.get_user_cube().draw_cube(qp)
        # Box of the room
        qp.drawLine(0, 0, self.size().width(), 0)
        qp.drawLine(self.size().width(), 0, self.size().width(), self.size().height())
        qp.drawLine(self.size().width(), self.size().height(), 0, self.size().height())
        qp.drawLine(0, self.size().height(), 0, 0)

        # Draw bad and room
        # My room
        qp.drawLine(0, 200, 100, 200)
        qp.drawLine(140, 200, 200, 200)
        qp.drawLine(200, 200, 200, 0)

        # Bad
        qp.drawLine(0, 50, 100, 50)
        qp.drawLine(100, 50, 100, 0)
        # Draw schoolbag
        qp.drawLine(200, 100, 150, 100)
        qp.drawLine(150, 100, 150, 150)
        qp.drawLine(150, 150, 200, 150)
        # Draw toilet
        qp.drawLine(200, 200, self.size().width()-100, 200)
        qp.drawLine(self.size().width()-50, 200, self.size().width(), 200)
        # Draw kitchen
        qp.drawLine(0, 300, 200, 300)
        qp.drawLine(200, 300, 200, self.size().height() - 150)
        qp.drawLine(200, self.size().height() - 100, 200, self.size().height())
        # Draw exist
        qp.drawLine(self.size().width()-100, self.size().height(), self.size().width()-100, self.size().height()-50)
        qp.drawLine(self.size().width()-50, self.size().height(), self.size().width()-50, self.size().height()-50)

