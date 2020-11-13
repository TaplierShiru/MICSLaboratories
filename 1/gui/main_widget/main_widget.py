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


class Ui_Main_widget(object):
    def setupUi(self, Main_widget):
        if not Main_widget.objectName():
            Main_widget.setObjectName(u"Main_widget")
        Main_widget.resize(946, 368)
        self.gridLayoutWidget = QWidget(Main_widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 912, 347))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_draw_dist = QPushButton(self.gridLayoutWidget)
        self.pushButton_draw_dist.setObjectName(u"pushButton_draw_dist")

        self.gridLayout.addWidget(self.pushButton_draw_dist, 4, 3, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_a = QLabel(self.gridLayoutWidget)
        self.label_a.setObjectName(u"label_a")

        self.verticalLayout.addWidget(self.label_a)

        self.label_b = QLabel(self.gridLayoutWidget)
        self.label_b.setObjectName(u"label_b")

        self.verticalLayout.addWidget(self.label_b)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_enter_a = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_enter_a.setObjectName(u"lineEdit_enter_a")

        self.verticalLayout_2.addWidget(self.lineEdit_enter_a)

        self.lineEdit_enter_b = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_enter_b.setObjectName(u"lineEdit_enter_b")

        self.verticalLayout_2.addWidget(self.lineEdit_enter_b)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_execute = QPushButton(self.gridLayoutWidget)
        self.pushButton_execute.setObjectName(u"pushButton_execute")

        self.verticalLayout_6.addWidget(self.pushButton_execute)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 4, 1, 1)

        self.label_friq_elem = QLabel(self.gridLayoutWidget)
        self.label_friq_elem.setObjectName(u"label_friq_elem")

        self.gridLayout.addWidget(self.label_friq_elem, 2, 3, 1, 1)

        self.textEdit_prob = QTextEdit(self.gridLayoutWidget)
        self.textEdit_prob.setObjectName(u"textEdit_prob")
        self.textEdit_prob.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_prob, 3, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_num_elements = QLabel(self.gridLayoutWidget)
        self.label_num_elements.setObjectName(u"label_num_elements")

        self.horizontalLayout_3.addWidget(self.label_num_elements)

        self.lineEdit_num_elements = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_num_elements.setObjectName(u"lineEdit_num_elements")

        self.horizontalLayout_3.addWidget(self.lineEdit_num_elements)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.label_list_of_gen_number = QLabel(self.gridLayoutWidget)
        self.label_list_of_gen_number.setObjectName(u"label_list_of_gen_number")

        self.gridLayout.addWidget(self.label_list_of_gen_number, 2, 1, 1, 1)

        self.label_prob = QLabel(self.gridLayoutWidget)
        self.label_prob.setObjectName(u"label_prob")

        self.gridLayout.addWidget(self.label_prob, 2, 4, 1, 1)

        self.pushButton_draw_elements = QPushButton(self.gridLayoutWidget)
        self.pushButton_draw_elements.setObjectName(u"pushButton_draw_elements")

        self.gridLayout.addWidget(self.pushButton_draw_elements, 4, 1, 1, 1)

        self.textEdit_friq_elements = QTextEdit(self.gridLayoutWidget)
        self.textEdit_friq_elements.setObjectName(u"textEdit_friq_elements")
        self.textEdit_friq_elements.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_friq_elements, 3, 3, 1, 1)

        self.pushButton_draw_histogram = QPushButton(self.gridLayoutWidget)
        self.pushButton_draw_histogram.setObjectName(u"pushButton_draw_histogram")

        self.gridLayout.addWidget(self.pushButton_draw_histogram, 4, 2, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetNoConstraint)
        self.label_mean = QLabel(self.gridLayoutWidget)
        self.label_mean.setObjectName(u"label_mean")

        self.verticalLayout_4.addWidget(self.label_mean)

        self.label_std = QLabel(self.gridLayoutWidget)
        self.label_std.setObjectName(u"label_std")

        self.verticalLayout_4.addWidget(self.label_std)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 2, 1, 1)

        self.textEdit_show_list_of_generated_nums = QTextEdit(self.gridLayoutWidget)
        self.textEdit_show_list_of_generated_nums.setObjectName(u"textEdit_show_list_of_generated_nums")
        self.textEdit_show_list_of_generated_nums.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit_show_list_of_generated_nums, 3, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit_mean = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_mean.setObjectName(u"lineEdit_mean")

        self.verticalLayout_5.addWidget(self.lineEdit_mean)

        self.lineEdit_std = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_std.setObjectName(u"lineEdit_std")

        self.verticalLayout_5.addWidget(self.lineEdit_std)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.label_hi_sqr = QLabel(self.gridLayoutWidget)
        self.label_hi_sqr.setObjectName(u"label_hi_sqr")

        self.verticalLayout_7.addWidget(self.label_hi_sqr)

        self.lineEdit_hi_sqr_value = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_hi_sqr_value.setObjectName(u"lineEdit_hi_sqr_value")
        self.lineEdit_hi_sqr_value.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.lineEdit_hi_sqr_value)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_7, 3, 2, 1, 1)


        self.retranslateUi(Main_widget)

        QMetaObject.connectSlotsByName(Main_widget)
    # setupUi

    def retranslateUi(self, Main_widget):
        Main_widget.setWindowTitle(QCoreApplication.translate("Main_widget", u"Form", None))
        self.pushButton_draw_dist.setText(QCoreApplication.translate("Main_widget", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label_a.setText(QCoreApplication.translate("Main_widget", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 a:", None))
        self.label_b.setText(QCoreApplication.translate("Main_widget", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 b:", None))
        self.pushButton_execute.setText(QCoreApplication.translate("Main_widget", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.label_friq_elem.setText(QCoreApplication.translate("Main_widget", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0432 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u044b:", None))
        self.label_num_elements.setText(QCoreApplication.translate("Main_widget", u"\u041a\u043e\u043b-\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432:", None))
        self.label_list_of_gen_number.setText(QCoreApplication.translate("Main_widget", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.label_prob.setText(QCoreApplication.translate("Main_widget", u"\u0422\u0435\u043e\u0440. \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u043f\u0430\u0434\u0435\u043d\u0438\u044f", None))
        self.pushButton_draw_elements.setText(QCoreApplication.translate("Main_widget", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c \u0432\u044b\u0431\u043e\u0440\u043a\u0443", None))
        self.pushButton_draw_histogram.setText(QCoreApplication.translate("Main_widget", u"\u0413\u0438\u0441\u0442\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.label_mean.setText(QCoreApplication.translate("Main_widget", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e:", None))
        self.label_std.setText(QCoreApplication.translate("Main_widget", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 std:", None))
        self.label_hi_sqr.setText(QCoreApplication.translate("Main_widget", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0445\u0438-\u043a\u0432\u0430\u0434\u0440\u0430\u0442", None))
    # retranslateUi

