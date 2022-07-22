# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entry.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QWidget)
import myres_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(248, 245, 238);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.new_button = QPushButton(self.centralwidget)
        self.new_button.setObjectName(u"new_button")
        self.new_button.setGeometry(QRect(432, 210, 160, 50))
        self.new_button.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(248, 245, 238);\n"
"font: 700 22pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"border-radius: 5px;")
        self.old_button = QPushButton(self.centralwidget)
        self.old_button.setObjectName(u"old_button")
        self.old_button.setGeometry(QRect(432, 310, 160, 50))
        self.old_button.setStyleSheet(u"background-color: rgb(178, 201, 171);\n"
"color: rgb(248, 245, 238);\n"
"font: 700 22pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"border-radius: 5px;")
        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setGeometry(QRect(332, 60, 360, 110))
        font = QFont()
        font.setFamilies([u"Palace Script MT"])
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(True)
        self.logo_label.setFont(font)
        self.logo_label.setStyleSheet(u"font-weight: bold;")
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.background_label = QLabel(self.centralwidget)
        self.background_label.setObjectName(u"background_label")
        self.background_label.setGeometry(QRect(0, 199, 1024, 381))
        self.background_label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.517045, y1:1, x2:0.466, y2:0, stop:0 rgba(178, 201, 171, 255), stop:1 rgba(248, 245, 238, 255));")
        self.background_label.setMidLineWidth(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.background_label.raise_()
        self.new_button.raise_()
        self.old_button.raise_()
        self.logo_label.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.new_button.clicked.connect(MainWindow.new_plant)
        self.old_button.clicked.connect(MainWindow.old_plant)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.new_button.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.old_button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.logo_label.setText(QCoreApplication.translate("MainWindow", u"Supool", None))
        self.background_label.setText("")
    # retranslateUi

