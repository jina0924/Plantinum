# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
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
    QSizePolicy, QWidget)
import myres_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 800)
        Form.setStyleSheet(u"")
        self.clock = QLabel(Form)
        self.clock.setObjectName(u"clock")
        self.clock.setGeometry(QRect(180, 180, 121, 71))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.clock.setFont(font)
        self.clock.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(70, 139, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.clock.setFrameShape(QFrame.NoFrame)
        self.clock.setAlignment(Qt.AlignCenter)
        self.clock.setWordWrap(False)
        self.page1 = QLabel(Form)
        self.page1.setObjectName(u"page1")
        self.page1.setGeometry(QRect(30, 30, 151, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.page1.setFont(font1)
        self.water = QLabel(Form)
        self.water.setObjectName(u"water")
        self.water.setGeometry(QRect(49, 135, 371, 461))
        font2 = QFont()
        font2.setBold(True)
        font2.setUnderline(False)
        self.water.setFont(font2)
        self.water.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.812, x2:1, y2:0, stop:0 rgba(82, 188, 254, 255), stop:1 rgba(255, 231, 210, 255));\n"
"\n"
"border-image: url(:/water/img/ocean.jpg);")
        self.water.setFrameShape(QFrame.NoFrame)
        self.water.setScaledContents(False)
        self.water.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.water.setWordWrap(False)
        self.exit_button = QPushButton(Form)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(270, 640, 111, 41))
        self.exit_button.setStyleSheet(u"background-color: rgb(255, 237, 222);\n"
"color: rgb(85, 170, 127);")
        self.exit_button_2 = QPushButton(Form)
        self.exit_button_2.setObjectName(u"exit_button_2")
        self.exit_button_2.setGeometry(QRect(100, 640, 111, 41))
        self.exit_button_2.setStyleSheet(u"background-color: rgb(255, 237, 222);\n"
"color: rgb(85, 170, 127);")
        self.page1.raise_()
        self.water.raise_()
        self.clock.raise_()
        self.exit_button.raise_()
        self.exit_button_2.raise_()

        self.retranslateUi(Form)
        self.exit_button.clicked.connect(Form.exit_program)
        self.exit_button_2.clicked.connect(Form.go_detailPage)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.clock.setText(QCoreApplication.translate("Form", u"12 : 00", None))
        self.page1.setText(QCoreApplication.translate("Form", u"MAIN", None))
        self.water.setText("")
        self.exit_button.setText(QCoreApplication.translate("Form", u"EXIT", None))
        self.exit_button_2.setText(QCoreApplication.translate("Form", u"Detail", None))
    # retranslateUi

