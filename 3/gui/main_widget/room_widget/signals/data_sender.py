from PySide2.QtCore import Signal, QObject


class DataSender(QObject):

    send_brain_strength = Signal(int)
    send_lucky = Signal(int)
    send_cur_state = Signal(int)
    send_remain_time = Signal(int)

    game_finished = Signal()
    game_finished_info = Signal(str)


