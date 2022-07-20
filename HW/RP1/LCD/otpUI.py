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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import myres_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 800)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.text_otp = QTextEdit(Form)
        self.text_otp.setObjectName(u"text_otp")
        self.text_otp.setGeometry(QRect(120, 350, 241, 71))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.text_otp.setFont(font)
        self.text_otp.setStyleSheet(u"border-color: rgb(85, 170, 127);\n"
"gridline-color: rgb(85, 170, 127);")
        self.text_otp.setFrameShadow(QFrame.Plain)
        self.text_otp.setLineWidth(5)
        self.label_otp = QLabel(Form)
        self.label_otp.setObjectName(u"label_otp")
        self.label_otp.setGeometry(QRect(160, 220, 161, 51))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.label_otp.setFont(font1)
        self.label_otp.setStyleSheet(u"background-color: rgba(255, 237, 216, 200);\n"
"color: rgb(85, 170, 0);")
        self.label_otp.setAlignment(Qt.AlignCenter)
        self.button_ok = QPushButton(Form)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setGeometry(QRect(180, 500, 121, 41))
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.button_ok.setFont(font2)
        self.button_ok.setStyleSheet(u"background-color: rgb(255, 235, 219);\n"
"color: rgb(85, 170, 127);")
        self.button_back = QPushButton(Form)
        self.button_back.setObjectName(u"button_back")
        self.button_back.setGeometry(QRect(20, 30, 81, 81))
        self.button_back.setFont(font2)
        self.button_back.setStyleSheet(u"background-color: rgb(255, 235, 219);\n"
"color: rgb(85, 170, 127);\n"
"border-image: url(:/icon/img/backicon.png);")

        self.retranslateUi(Form)
        self.button_ok.clicked.connect(Form.check_otp)
        self.button_back.clicked.connect(Form.back_entry)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.text_otp.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:20pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_otp.setText(QCoreApplication.translate("Form", u"OTP", None))
        self.button_ok.setText(QCoreApplication.translate("Form", u"ok", None))
        self.button_back.setText("")
    # retranslateUi

