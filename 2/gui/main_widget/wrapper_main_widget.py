from gui.main_widget.main_widget import Ui_Form
from num_generation.data_collector import DataCollector
from gui.generation_pool import GeneratWorker
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QThreadPool


class Main_widget(QWidget):
    def __init__(self, parent):
        super(Main_widget, self).__init__(parent=parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.pool = QThreadPool()
        #print("Multithreading with maximum %d threads" % self.pool.maxThreadCount())

        self.setLayout(self.ui.gridLayout)
        self.connect_events()

        self.avg_past_list = []
        self.ui.pushButton_drop_avg.clicked.connect(self.__restore_avg_counter)

    def connect_events(self):
        self.ui.pushButton_start.clicked.connect(self.generate_numbers)

    def generate_numbers(self):
        first = DataCollector(float(self.ui.lineEdit_first_a.text()), float(self.ui.lineEdit_fisrt_b.text()))
        second = DataCollector(float(self.ui.lineEdit_second_a.text()), float(self.ui.lineEdit_second_b.text()))
        time = float(self.ui.lineEdit_time.text())

        worker = GeneratWorker(first, second, time)
        worker.signals.result.connect(self.print_final_data)
        worker.signals.finished.connect(lambda: print('Finished'))
        self.pool.start(worker)

    def print_final_data(self, worker: GeneratWorker):

        # Считаем среднее и выводим
        self.avg_past_list += [min(len(worker.first), len(worker.second))]
        self.ui.lineEdit_num_past.setText(str(sum(self.avg_past_list) // len(self.avg_past_list)))

        # Выводим значения из моделируемых распределений и их сумму
        first = sorted(worker.first)
        second = sorted(worker.second)

        first_text = ""
        for i, elem in enumerate(first):
            first_text += f'{i+1}) ' + str(round(elem, 3)) + "\n"

        second_text = ""
        for i, elem in enumerate(second):
            second_text += f'{i+1}) ' + str(round(elem, 3)) + "\n"

        sum_text = ""
        for i in range(min(len(first), len(second))):
            sum_text += f'{i+1}) ' + str(round(first[i] + second[i], 3)) + "\n"

        self.ui.plainTextEdit_first_dist.setPlainText(first_text)
        self.ui.plainTextEdit_second_dist.setPlainText(second_text)
        self.ui.plainTextEdit_sum.setPlainText(sum_text)

    def __restore_avg_counter(self):
        self.avg_past_list = []
