# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(856, 500)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 831, 481))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_second_b = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_second_b.setObjectName(u"lineEdit_second_b")

        self.gridLayout.addWidget(self.lineEdit_second_b, 1, 4, 1, 1)

        self.plainTextEdit_first_dist = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_first_dist.setObjectName(u"plainTextEdit_first_dist")

        self.gridLayout.addWidget(self.plainTextEdit_first_dist, 5, 0, 1, 1)

        self.lineEdit_fisrt_b = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_fisrt_b.setObjectName(u"lineEdit_fisrt_b")

        self.gridLayout.addWidget(self.lineEdit_fisrt_b, 0, 4, 1, 1)

        self.label_time = QLabel(self.gridLayoutWidget)
        self.label_time.setObjectName(u"label_time")

        self.gridLayout.addWidget(self.label_time, 2, 1, 1, 1)

        self.label_first_dist_param = QLabel(self.gridLayoutWidget)
        self.label_first_dist_param.setObjectName(u"label_first_dist_param")

        self.gridLayout.addWidget(self.label_first_dist_param, 0, 0, 1, 1)

        self.label_first_dist = QLabel(self.gridLayoutWidget)
        self.label_first_dist.setObjectName(u"label_first_dist")

        self.gridLayout.addWidget(self.label_first_dist, 3, 0, 1, 1)

        self.lineEdit_time = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_time.setObjectName(u"lineEdit_time")

        self.gridLayout.addWidget(self.lineEdit_time, 2, 2, 1, 1)

        self.label_second_a = QLabel(self.gridLayoutWidget)
        self.label_second_a.setObjectName(u"label_second_a")
        self.label_second_a.setAutoFillBackground(True)
        self.label_second_a.setScaledContents(False)
        self.label_second_a.setWordWrap(False)

        self.gridLayout.addWidget(self.label_second_a, 1, 1, 1, 1)

        self.lineEdit_num_past = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_num_past.setObjectName(u"lineEdit_num_past")
        self.lineEdit_num_past.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_num_past, 6, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 3, 1, 1)

        self.label_num_past = QLabel(self.gridLayoutWidget)
        self.label_num_past.setObjectName(u"label_num_past")

        self.gridLayout.addWidget(self.label_num_past, 6, 0, 1, 1)

        self.label_second_b = QLabel(self.gridLayoutWidget)
        self.label_second_b.setObjectName(u"label_second_b")

        self.gridLayout.addWidget(self.label_second_b, 1, 3, 1, 1)

        self.lineEdit_second_a = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_second_a.setObjectName(u"lineEdit_second_a")

        self.gridLayout.addWidget(self.lineEdit_second_a, 1, 2, 1, 1)

        self.lineEdit_first_a = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_first_a.setObjectName(u"lineEdit_first_a")

        self.gridLayout.addWidget(self.lineEdit_first_a, 0, 2, 1, 1)

        self.label_second_dist_param = QLabel(self.gridLayoutWidget)
        self.label_second_dist_param.setObjectName(u"label_second_dist_param")

        self.gridLayout.addWidget(self.label_second_dist_param, 1, 0, 1, 1)

        self.label_first_a = QLabel(self.gridLayoutWidget)
        self.label_first_a.setObjectName(u"label_first_a")

        self.gridLayout.addWidget(self.label_first_a, 0, 1, 1, 1)

        self.label_first_b = QLabel(self.gridLayoutWidget)
        self.label_first_b.setObjectName(u"label_first_b")

        self.gridLayout.addWidget(self.label_first_b, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 5, 1, 1)

        self.pushButton_start = QPushButton(self.gridLayoutWidget)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.gridLayout.addWidget(self.pushButton_start, 6, 5, 1, 1)

        self.label_second_dist = QLabel(self.gridLayoutWidget)
        self.label_second_dist.setObjectName(u"label_second_dist")

        self.gridLayout.addWidget(self.label_second_dist, 3, 2, 1, 1)

        self.plainTextEdit_second_dist = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_second_dist.setObjectName(u"plainTextEdit_second_dist")
        self.plainTextEdit_second_dist.setEnabled(True)

        self.gridLayout.addWidget(self.plainTextEdit_second_dist, 5, 2, 1, 1)

        self.label_sum = QLabel(self.gridLayoutWidget)
        self.label_sum.setObjectName(u"label_sum")

        self.gridLayout.addWidget(self.label_sum, 3, 4, 1, 1)

        self.plainTextEdit_sum = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_sum.setObjectName(u"plainTextEdit_sum")

        self.gridLayout.addWidget(self.plainTextEdit_sum, 5, 4, 1, 1)

        self.pushButton_drop_avg = QPushButton(self.gridLayoutWidget)
        self.pushButton_drop_avg.setObjectName(u"pushButton_drop_avg")

        self.gridLayout.addWidget(self.pushButton_drop_avg, 6, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_time.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f:", None))
        self.label_first_dist_param.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0432\u043e\u0435 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label_first_dist.setText(QCoreApplication.translate("Form", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.label_second_a.setText(QCoreApplication.translate("Form", u"a:", None))
        self.label_num_past.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u043f\u0440\u043e\u0448\u0435\u0434\u0448\u0438\u043a \u0437\u0430\u044f\u0432\u043e\u043a", None))
        self.label_second_b.setText(QCoreApplication.translate("Form", u"b:", None))
        self.label_second_dist_param.setText(QCoreApplication.translate("Form", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label_first_a.setText(QCoreApplication.translate("Form", u"a:", None))
        self.label_first_b.setText(QCoreApplication.translate("Form", u"b:", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"Start", None))
        self.label_second_dist.setText(QCoreApplication.translate("Form", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.label_sum.setText(QCoreApplication.translate("Form", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.pushButton_drop_avg.setText(QCoreApplication.translate("Form", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0441\u0447\u0451\u0442\u0447\u0438\u043a", None))
    # retranslateUi

