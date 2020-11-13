
from PySide2.QtWidgets import *
import matplotlib.pyplot as plt
from num_generation import DataCollector
from .main_widget import Ui_Main_widget


class Main_widget(QWidget):

    def __init__(self, parent):
        super(Main_widget, self).__init__(parent)
        self.ui = Ui_Main_widget()
        self.ui.setupUi(self)

        self.data_collector = DataCollector()
        self.setUp_connection()

    def _generate_new_numbers(self):
        a = float(self.ui.lineEdit_enter_a.text())
        b = float(self.ui.lineEdit_enter_b.text())
        mean = float(self.ui.lineEdit_mean.text())
        std = float(self.ui.lineEdit_std.text())
        n = int(self.ui.lineEdit_num_elements.text())
        self.data_collector.regenerate_numbers(
            n=n,
            a=a,
            b=b,
            mu=mean,
            std=std
        )
        self.data_collector.collect_data_from_dist()

        numText = ""
        numbers = self.data_collector.read_numbers()
        for single_num in numbers:
            numText += str(single_num) + "\n"

        friqText = ""
        friq_list = self.data_collector.friq_list
        for i, single_num in enumerate(friq_list):
            friqText += f"{i+1}: " + str(single_num) + "\n"

        probText = ""
        prob_list = self.data_collector.prob_list
        for i, single_num in enumerate(prob_list):
            probText += f"{i+1}: " + str(single_num) + "\n"

        self.ui.textEdit_show_list_of_generated_nums.setText(numText)
        self.ui.textEdit_friq_elements.setText(friqText)
        self.ui.textEdit_prob.setText(probText)
        self.ui.lineEdit_hi_sqr_value.setText(str(round(self.data_collector.x_watch, 4)))

    def _draw_numbers(self):
        image_of_numbers = self.data_collector.draw_numbers()
        plt.imshow(image_of_numbers)
        plt.axis('off')
        plt.show()

    def _draw_histogram(self):
        image_of_hist = self.data_collector.draw_histograme()
        plt.imshow(image_of_hist)
        plt.axis('off')
        plt.show()

    def _draw_dist(self):
        image_of_dist = self.data_collector.draw_dist()
        plt.imshow(image_of_dist)
        plt.axis('off')
        plt.show()

    def setUp_connection(self):
        self.ui.pushButton_draw_histogram.clicked.connect(self._draw_histogram)
        self.ui.pushButton_execute.clicked.connect(self._generate_new_numbers)
        self.ui.pushButton_draw_elements.clicked.connect(self._draw_numbers)
        self.ui.pushButton_draw_dist.clicked.connect(self._draw_dist)
