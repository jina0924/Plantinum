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
#from PySide6.QtUiTools import *
#from PyQt6.QtWidgets import QGraphicsOpacityEffect


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 600)
        Form.setStyleSheet(u"")

        # 시계
        self.clock = QLabel(Form)
        self.clock.setObjectName(u"clock")
        self.clock.setGeometry(QRect(362, 15, 300, 70))
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.clock.setFont(font)
        self.clock.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(70, 139, 0);\n"
"color: rgb(255, 255, 255);\n"
"text-shadow: 2px 2px 2px gray;\n")
        self.clock.setFrameShape(QFrame.NoFrame)
        self.clock.setAlignment(Qt.AlignCenter)
        self.clock.setWordWrap(False)

        self.page1 = QLabel(Form)
        self.page1.setObjectName(u"page1")
        self.page1.setGeometry(QRect(30, 30, 151, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.page1.setFont(font1)

        #검은 바
        self.bgbar = QLabel(Form)
        self.bgbar.setObjectName(u"clock")
        self.bgbar.setGeometry(QRect(0, 0, 1024, 600))
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.bgbar.setFont(font)
        self.bgbar.setStyleSheet(u"background-color: rgba(0, 0, 100, 20);\n")
        self.bgbar.setFrameShape(QFrame.NoFrame)
        self.bgbar.setAlignment(Qt.AlignCenter)
        self.bgbar.setWordWrap(False)

        # 배경화면
        self.water = QLabel(Form)
        self.water.setObjectName(u"water")
        self.water.setGeometry(QRect(0, 0, 1024, 600))
        font2 = QFont()
        font2.setBold(True)
        font2.setUnderline(False)
        self.water.setFont(font2)
        self.water.setStyleSheet(u"\n"
        "background-color: qlineargradient(spread:pad, x1:1, y1:0.812, x2:1, y2:0, stop:0 rgba(82, 188, 254, 255), stop:1 rgba(255, 231, 210, 255));\n"
        "\n"
        "border-image: url(./img/background_sand.jpg);")
        self.water.setFrameShape(QFrame.NoFrame)
        self.water.setScaledContents(False)
        self.water.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.water.setWordWrap(False)

        # 알림 버튼
        self.notice_button = QPushButton(Form)
        self.notice_button.setObjectName(u"notice_button")
        self.notice_button.setStyleSheet(u"\n"
        "border-image: url(./img/bell_white.png);")
        self.notice_button.setGeometry(QRect(20, 20, 40, 40))

        # 수분 버튼 // 대기 습도
        self.waterLV_button = QPushButton(Form)
        self.waterLV_button.setObjectName(u"notice_button")
        self.waterLV_button.setStyleSheet(u"\n"
        "border-image: url(./img/water_white.png);")
        self.waterLV_button.setGeometry(QRect(900, 20, 40, 40))

        # 수분 라벨 // 대기 습도
        self.waterLV_label = QLabel(Form)
        self.waterLV_label.setObjectName(u"water_label")
        self.waterLV_label.setText("80")
        self.waterLV_label.setGeometry(QRect(940, 15, 50, 50))

        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)

        self.waterLV_label.setFont(font2)
        self.waterLV_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                 "color: rgb(255, 255, 255);\n")
        self.waterLV_label.setFrameShape(QFrame.NoFrame)
        self.waterLV_label.setAlignment(Qt.AlignCenter)
        self.waterLV_label.setWordWrap(False)


        # 온도 버튼
        self.temper_button = QPushButton(Form)
        self.temper_button.setObjectName(u"notice_button")
        self.temper_button.setStyleSheet(u"\n"
        "border-image: url(./img/temperature_white.png);")
        self.temper_button.setGeometry(QRect(800, 20, 40, 40))

        #온도 라벨
        self.temp_label = QLabel(Form)
        self.temp_label.setObjectName(u"water_label")
        self.temp_label.setText("20")
        self.temp_label.setGeometry(QRect(840, 15, 50, 50))

        self.temp_label.setFont(font2)
        self.temp_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                         "color: rgb(255, 255, 255);\n")
        self.temp_label.setFrameShape(QFrame.NoFrame)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.temp_label.setWordWrap(False)

        # 종료 버튼
        # 이걸 없애면 자꾸 오류가 떠서 일단 보이지 않는 쪽으로 넣어뒀습니다.
        # 600 pixel 아래에 있어요
        self.exit_button = QPushButton(Form)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(270, 640, 111, 41))
        self.exit_button.setStyleSheet(u"background-color: rgb(255, 237, 222);\n"
        "color: rgb(85, 170, 127);")

        # detail 버튼
        # 화면 전체 중 아무곳이나 클릭했을 때 detail page로 넘어가면 좋겠어서
        # 아예 전체 투명화를 해버렸습니다.
        self.exit_button_2 = QPushButton(Form)
        self.exit_button_2.setObjectName(u"exit_button_2")
        self.exit_button_2.setGeometry(QRect(0, 0, 1024, 600))
        self.exit_button_2.setStyleSheet(u"background: transparent;\n"
        "color: transparent;")

        # 파도
        self.wave = QLabel(Form)
        self.wave.setObjectName(u"wave")
        # 아래의 setGeometry 중 300 부분을 조정해주시면 됩니다.
        self.wave.setGeometry(QRect(0, 300, 1024, 600))

        self.wave.setFont(font2)
        self.wave.setStyleSheet(u"\n"
                                 "background: transparent;\n"
                                 "\n"
                                 "border-image: url(./img/wave.png);")
        self.wave.setFrameShape(QFrame.NoFrame)
        self.wave.setScaledContents(False)
        self.wave.setAlignment(Qt.AlignJustify | Qt.AlignVCenter)
        self.wave.setWordWrap(False)


        # 경로 라벨
        self.warn_label = QLabel(Form)
        self.warn_label.setObjectName(u"water_label")
        self.warn_label.setText("물통에 물을 채워주세요")
        self.warn_label.setGeometry(QRect(50, 15, 300, 50))

        self.warn_label.setFont(font1)
        self.warn_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                      "color: rgb(255, 255, 255);\n")
        self.warn_label.setFrameShape(QFrame.NoFrame)
        self.warn_label.setAlignment(Qt.AlignCenter)
        self.warn_label.setWordWrap(False)


        self.page1.raise_()
        self.water.raise_()

        self.wave.raise_()
        self.bgbar.raise_()
        self.clock.raise_()
        self.exit_button.raise_()
        self.exit_button_2.raise_()
        self.notice_button.raise_()
        self.temper_button.raise_()
        self.waterLV_button.raise_()
        self.waterLV_label.raise_()
        self.temp_label.raise_()
        self.warn_label.raise_()


        self.retranslateUi(Form)
        self.exit_button.clicked.connect(Form.exit_program)
        self.exit_button_2.clicked.connect(Form.go_detailPage)
        #self.exit_button.setGeometry(QRect(270, 640, 111, 41))
        #self.exit_button.setStyleSheet(u"background-color: rgb(255, 237, 222);\n"

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




#app = QApplication()
#main = QUiLoader().load("mainUI.ui")

#main.show()
#app.exec()