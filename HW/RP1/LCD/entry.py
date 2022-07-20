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
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import myres_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 800)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.new_button = QPushButton(self.centralwidget)
        self.new_button.setObjectName(u"new_button")
        self.new_button.setGeometry(QRect(120, 310, 251, 91))
        self.new_button.setStyleSheet(u"background-color: rgb(255, 237, 222);\n"
"color: rgb(85, 170, 127);\n"
"font: 16pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.old_button = QPushButton(self.centralwidget)
        self.old_button.setObjectName(u"old_button")
        self.old_button.setGeometry(QRect(120, 490, 251, 101))
        self.old_button.setStyleSheet(u"background-color: rgb(255, 237, 222);\n"
"color: rgb(85, 170, 127);\n"
"font: 16pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 321, 221))
        self.label.setStyleSheet(u"\n"
"image: url(:/logo/img/logo.png);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.new_button.clicked.connect(MainWindow.new_plant)
        self.old_button.clicked.connect(MainWindow.old_plant)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.new_button.setText(QCoreApplication.translate("MainWindow", u"NEW", None))
        self.old_button.setText(QCoreApplication.translate("MainWindow", u"EXIST", None))
        self.label.setText("")
    # retranslateUi

