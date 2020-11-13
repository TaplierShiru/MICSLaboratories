from .signal_sender import SignalSender
from num_generation import DataCollector

from PySide2.QtCore import QRunnable
from PySide2.QtCore import Slot

import traceback, sys


class GeneratWorker(QRunnable):

    def __init__(self, first: DataCollector, second: DataCollector, time: float):
        super(GeneratWorker, self).__init__()
        self.first = []
        self.second = []

        self.data_col_first = first
        self.data_col_second = second
        self.time = time

        self.signals = SignalSender()

    @Slot()
    def run(self):
        try:
            past_time = 0.0
            while True:
                self.first += [self.data_col_first.generate_single()]
                past_time += self.first[-1]
                if past_time > self.time:
                    break
                self.second += [self.data_col_second.generate_single()]
                past_time += self.second[-1]
                if past_time > self.time:
                    break
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(self)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

