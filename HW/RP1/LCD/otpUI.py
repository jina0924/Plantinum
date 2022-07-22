# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'otpUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QWidget)
import myres_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 600)
        Form.setStyleSheet(u"background-color: rgb(248, 245, 238);")
        self.label_otp = QLabel(Form)
        self.label_otp.setObjectName(u"label_otp")
        self.label_otp.setGeometry(QRect(156, 130, 200, 80))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        self.label_otp.setFont(font)
        self.label_otp.setStyleSheet(u"background-color: rgba(255, 237, 216,0);\n"
"color: rgb(101, 128, 93);")
        self.label_otp.setAlignment(Qt.AlignCenter)
        self.button_ok = QPushButton(Form)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setGeometry(QRect(690, 490, 121, 41))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.button_ok.setFont(font1)
        self.button_ok.setStyleSheet(u"background-color: rgb(255, 235, 219);\n"
"color: rgb(85, 170, 127);")
        self.button_back = QPushButton(Form)
        self.button_back.setObjectName(u"button_back")
        self.button_back.setGeometry(QRect(950, 20, 41, 41))
        self.button_back.setFont(font1)
        self.button_back.setStyleSheet(u"background-color: rgb(248, 245, 238);\n"
"color: rgb(85, 170, 127);\n"
"border-image: url(:/icon/img/backicon.png);")
        self.logo_label = QLabel(Form)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(20, 20, 81, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(16, 240, 480, 20))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(101, 128, 93);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 310, 321, 71))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setContentsMargins(1, 0, 0, 0)
        self.number_4 = QLabel(self.widget)
        self.number_4.setObjectName(u"number_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_4.sizePolicy().hasHeightForWidth())
        self.number_4.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(26)
        font3.setBold(True)
        self.number_4.setFont(font3)
        self.number_4.setStyleSheet(u"background-color : white;\n"
"border-radius: 10px;\n"
"")
        self.number_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.number_4, 0, 4, 1, 1)

        self.number_1 = QLabel(self.widget)
        self.number_1.setObjectName(u"number_1")
        sizePolicy.setHeightForWidth(self.number_1.sizePolicy().hasHeightForWidth())
        self.number_1.setSizePolicy(sizePolicy)
        self.number_1.setFont(font3)
        self.number_1.setStyleSheet(u"background-color : white;\n"
"border-radius: 10px;\n"
"")
        self.number_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.number_1, 0, 0, 1, 1)

        self.number_2 = QLabel(self.widget)
        self.number_2.setObjectName(u"number_2")
        sizePolicy.setHeightForWidth(self.number_2.sizePolicy().hasHeightForWidth())
        self.number_2.setSizePolicy(sizePolicy)
        self.number_2.setFont(font3)
        self.number_2.setStyleSheet(u"background-color : white;\n"
"border-radius: 10px;\n"
"")
        self.number_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.number_2, 0, 2, 1, 1)

        self.number_3 = QLabel(self.widget)
        self.number_3.setObjectName(u"number_3")
        sizePolicy.setHeightForWidth(self.number_3.sizePolicy().hasHeightForWidth())
        self.number_3.setSizePolicy(sizePolicy)
        self.number_3.setFont(font3)
        self.number_3.setStyleSheet(u"background-color : white;\n"
"border-radius: 10px;\n"
"")
        self.number_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.number_3, 0, 3, 1, 1)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(610, 70, 301, 371))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.pad_3 = QPushButton(self.widget1)
        self.pad_3.setObjectName(u"pad_3")
        sizePolicy.setHeightForWidth(self.pad_3.sizePolicy().hasHeightForWidth())
        self.pad_3.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.pad_3.setFont(font4)
        self.pad_3.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_3, 0, 2, 1, 1)

        self.pad_1 = QPushButton(self.widget1)
        self.pad_1.setObjectName(u"pad_1")
        self.pad_1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pad_1.sizePolicy().hasHeightForWidth())
        self.pad_1.setSizePolicy(sizePolicy)
        self.pad_1.setFont(font4)
        self.pad_1.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_1, 0, 0, 1, 1)

        self.pad_7 = QPushButton(self.widget1)
        self.pad_7.setObjectName(u"pad_7")
        sizePolicy.setHeightForWidth(self.pad_7.sizePolicy().hasHeightForWidth())
        self.pad_7.setSizePolicy(sizePolicy)
        self.pad_7.setFont(font4)
        self.pad_7.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_7, 2, 0, 1, 1)

        self.pad_8 = QPushButton(self.widget1)
        self.pad_8.setObjectName(u"pad_8")
        sizePolicy.setHeightForWidth(self.pad_8.sizePolicy().hasHeightForWidth())
        self.pad_8.setSizePolicy(sizePolicy)
        self.pad_8.setFont(font4)
        self.pad_8.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_8, 2, 1, 1, 1)

        self.pad_ok = QPushButton(self.widget1)
        self.pad_ok.setObjectName(u"pad_ok")
        sizePolicy.setHeightForWidth(self.pad_ok.sizePolicy().hasHeightForWidth())
        self.pad_ok.setSizePolicy(sizePolicy)
        self.pad_ok.setFont(font4)
        self.pad_ok.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color: rgb(178, 201, 171);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_ok, 3, 2, 1, 1)

        self.pad_6 = QPushButton(self.widget1)
        self.pad_6.setObjectName(u"pad_6")
        sizePolicy.setHeightForWidth(self.pad_6.sizePolicy().hasHeightForWidth())
        self.pad_6.setSizePolicy(sizePolicy)
        self.pad_6.setFont(font4)
        self.pad_6.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_6, 1, 2, 1, 1)

        self.pad_0 = QPushButton(self.widget1)
        self.pad_0.setObjectName(u"pad_0")
        sizePolicy.setHeightForWidth(self.pad_0.sizePolicy().hasHeightForWidth())
        self.pad_0.setSizePolicy(sizePolicy)
        self.pad_0.setFont(font4)
        self.pad_0.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_0, 3, 1, 1, 1)

        self.pad_2 = QPushButton(self.widget1)
        self.pad_2.setObjectName(u"pad_2")
        sizePolicy.setHeightForWidth(self.pad_2.sizePolicy().hasHeightForWidth())
        self.pad_2.setSizePolicy(sizePolicy)
        self.pad_2.setFont(font4)
        self.pad_2.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_2, 0, 1, 1, 1)

        self.pad_9 = QPushButton(self.widget1)
        self.pad_9.setObjectName(u"pad_9")
        sizePolicy.setHeightForWidth(self.pad_9.sizePolicy().hasHeightForWidth())
        self.pad_9.setSizePolicy(sizePolicy)
        self.pad_9.setFont(font4)
        self.pad_9.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_9, 2, 2, 1, 1)

        self.pad_4 = QPushButton(self.widget1)
        self.pad_4.setObjectName(u"pad_4")
        sizePolicy.setHeightForWidth(self.pad_4.sizePolicy().hasHeightForWidth())
        self.pad_4.setSizePolicy(sizePolicy)
        self.pad_4.setFont(font4)
        self.pad_4.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_4, 1, 0, 1, 1)

        self.pad_back = QPushButton(self.widget1)
        self.pad_back.setObjectName(u"pad_back")
        sizePolicy.setHeightForWidth(self.pad_back.sizePolicy().hasHeightForWidth())
        self.pad_back.setSizePolicy(sizePolicy)
        self.pad_back.setFont(font4)
        self.pad_back.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color: rgb(178, 201, 171);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_back, 3, 0, 1, 1)

        self.pad_5 = QPushButton(self.widget1)
        self.pad_5.setObjectName(u"pad_5")
        sizePolicy.setHeightForWidth(self.pad_5.sizePolicy().hasHeightForWidth())
        self.pad_5.setSizePolicy(sizePolicy)
        self.pad_5.setFont(font4)
        self.pad_5.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(255,255,255);\n"
"border-radius:5px;")

        self.gridLayout_2.addWidget(self.pad_5, 1, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)

        self.retranslateUi(Form)
        self.button_ok.clicked.connect(Form.check_otp)
        self.button_back.clicked.connect(Form.back_entry)
        self.pad_ok.clicked.connect(Form.check_otp)
        self.pad_back.clicked.connect(Form.click_pad)
        self.pad_1.clicked.connect(Form.click_pad)
        self.pad_2.clicked.connect(Form.click_pad)
        self.pad_3.clicked.connect(Form.click_pad)
        self.pad_4.clicked.connect(Form.click_pad)
        self.pad_5.clicked.connect(Form.click_pad)
        self.pad_6.clicked.connect(Form.click_pad)
        self.pad_7.clicked.connect(Form.click_pad)
        self.pad_9.clicked.connect(Form.click_pad)
        self.pad_8.clicked.connect(Form.click_pad)
        self.pad_0.clicked.connect(Form.click_pad)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_otp.setText(QCoreApplication.translate("Form", u"OTP", None))
        self.button_ok.setText(QCoreApplication.translate("Form", u"ok", None))
        self.button_back.setText("")
        self.logo_label.setText(QCoreApplication.translate("Form", u"plantinum", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\uc6f9 \ud654\uba74\uc5d0 \ud45c\uc2dc\ub41c \uc22b\uc790\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.number_4.setText(QCoreApplication.translate("Form", u"1", None))
        self.number_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.number_2.setText(QCoreApplication.translate("Form", u"1", None))
        self.number_3.setText(QCoreApplication.translate("Form", u"1", None))
        self.pad_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pad_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pad_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pad_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pad_ok.setText(QCoreApplication.translate("Form", u"ok", None))
        self.pad_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pad_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pad_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pad_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pad_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pad_back.setText(QCoreApplication.translate("Form", u"<", None))
        self.pad_5.setText(QCoreApplication.translate("Form", u"5", None))
    # retranslateUi

