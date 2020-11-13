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
from .room_widget import QRoomFrame as QFrame


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(786, 530)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 761, 511))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_info_about_game = QLabel(self.gridLayoutWidget)
        self.label_info_about_game.setObjectName(u"label_info_about_game")

        self.verticalLayout_2.addWidget(self.label_info_about_game)

        self.plainTextEdit_game_info = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_game_info.setObjectName(u"plainTextEdit_game_info")
        self.plainTextEdit_game_info.setReadOnly(True)
        self.verticalLayout_2.addWidget(self.plainTextEdit_game_info)

        self.verticalSpacer = QSpacerItem(20, 400, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 5, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.horizontalLayout_button = QHBoxLayout()
        self.horizontalLayout_button.setObjectName(u"horizontalLayout_button")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_button.addItem(self.horizontalSpacer)

        self.pushButton_start_game = QPushButton(self.gridLayoutWidget)
        self.pushButton_start_game.setObjectName(u"pushButton_start_game")

        self.horizontalLayout_button.addWidget(self.pushButton_start_game)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_button.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_button, 3, 3, 1, 1)

        self.horizontalLayout_common_lucky = QHBoxLayout()
        self.horizontalLayout_common_lucky.setObjectName(u"horizontalLayout_common_lucky")
        self.label_cur_lucky = QLabel(self.gridLayoutWidget)
        self.label_cur_lucky.setObjectName(u"label_cur_lucky")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cur_lucky.sizePolicy().hasHeightForWidth())
        self.label_cur_lucky.setSizePolicy(sizePolicy)

        self.horizontalLayout_common_lucky.addWidget(self.label_cur_lucky)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_common_lucky.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_common_lucky.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_common_lucky.addItem(self.horizontalSpacer_7)

        self.lineEdit_cur_lucky = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_cur_lucky.setObjectName(u"lineEdit_cur_lucky")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_cur_lucky.sizePolicy().hasHeightForWidth())
        self.lineEdit_cur_lucky.setSizePolicy(sizePolicy1)
        self.lineEdit_cur_lucky.setReadOnly(True)

        self.horizontalLayout_common_lucky.addWidget(self.lineEdit_cur_lucky)


        self.gridLayout.addLayout(self.horizontalLayout_common_lucky, 2, 1, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.horizontalLayout_commin_strength = QHBoxLayout()
        self.horizontalLayout_commin_strength.setObjectName(u"horizontalLayout_commin_strength")
        self.label_cur_brain = QLabel(self.gridLayoutWidget)
        self.label_cur_brain.setObjectName(u"label_cur_brain")

        self.horizontalLayout_commin_strength.addWidget(self.label_cur_brain)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_commin_strength.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_commin_strength.addItem(self.horizontalSpacer_10)

        self.lineEdit_cur_brain = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_cur_brain.setObjectName(u"lineEdit_cur_brain")
        sizePolicy.setHeightForWidth(self.lineEdit_cur_brain.sizePolicy().hasHeightForWidth())
        self.lineEdit_cur_brain.setSizePolicy(sizePolicy)
        self.lineEdit_cur_brain.setMinimumSize(QSize(10, 10))
        self.lineEdit_cur_brain.setReadOnly(True)

        self.horizontalLayout_commin_strength.addWidget(self.lineEdit_cur_brain)


        self.gridLayout.addLayout(self.horizontalLayout_commin_strength, 3, 1, 1, 2)

        self.frame_game_shower = QFrame(self.gridLayoutWidget)
        self.frame_game_shower.setObjectName(u"frame_game_shower")
        self.frame_game_shower.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_game_shower.sizePolicy().hasHeightForWidth())
        self.frame_game_shower.setSizePolicy(sizePolicy2)
        self.frame_game_shower.setMinimumSize(QSize(400, 200))
        self.frame_game_shower.setMaximumSize(QSize(400, 600))
        self.frame_game_shower.setFrameShape(QFrame.StyledPanel)
        self.frame_game_shower.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_game_shower, 5, 1, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.lcdNumber_timecount = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_timecount.setObjectName(u"lcdNumber_timecount")
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber_timecount.setFont(font)
        self.lcdNumber_timecount.setFrameShape(QFrame.WinPanel)
        self.lcdNumber_timecount.setFrameShadow(QFrame.Sunken)
        self.lcdNumber_timecount.setSmallDecimalPoint(False)

        self.horizontalLayout.addWidget(self.lcdNumber_timecount)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.label_timer = QLabel(self.gridLayoutWidget)
        self.label_timer.setObjectName(u"label_timer")

        self.horizontalLayout_2.addWidget(self.label_timer)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_13)

        self.label_cur_statictic = QLabel(self.gridLayoutWidget)
        self.label_cur_statictic.setObjectName(u"label_cur_statictic")

        self.horizontalLayout_3.addWidget(self.label_cur_statictic)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_info_about_game.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u0432 \u043c\u0438\u0440\u0435", None))
        self.pushButton_start_game.setText(QCoreApplication.translate("Form", u"Start", None))
        self.label_cur_lucky.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u0447\u0430", None))
        self.label_cur_brain.setText(QCoreApplication.translate("Form", u"\u0421\u0438\u043b\u0430 \u043c\u043e\u0437\u0433\u0430", None))
        self.label_timer.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u0439\u043c\u0435\u0440", None))
        self.label_cur_statictic.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430:", None))
    # retranslateUi

