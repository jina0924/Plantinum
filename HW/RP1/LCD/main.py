from PySide6.QtWidgets import *
from PySide6.QtCore import *
from entry import Ui_MainWindow
from mainUI import Ui_Form as Ui_MainUI
from detailUI import Ui_Form as Ui_DetailUI
from otpUI import Ui_Form as Ui_Otp

import mysql.connector
import json
from datetime import datetime




class EntryPage(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dbset()

    def dbset(self):
        global db
        db = mysql.connector.connect(host="localhost",user='root', password='111111', database='testdb',buffered=True)
        self.cur = db.cursor()
        self.cur.execute("select * from test")

    def main(self):
        pass

    def new_plant(self):
        #otp 등록페이지로 이동
        self.hide()
        print("regist new plant!")
        self.go_otp = OtpPage()
        self.go_otp.exec_()
        if(success_acc == 1):
            self.old_plant()
        else:
            self.show()

    def old_plant(self):
        #바로 메인페이지로 이동
        self.hide()
        print("go to main page!")
        self.second = MainPage()
        self.second.exec_()
        #self.close()
        # 메인페이지가 끝나면 바로 종료


class MainPage(QDialog, QWidget, Ui_MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("HI I'm MainPage")
        #self.show()
        #self.main()
        self.init()

    def init(self):
        self.timer_clock = QTimer()
        self.timer_clock.setInterval(1000) #1초
        self.timer_clock.timeout.connect(self.clock)
        self.timer_clock.start()


    def main(self):
        pass

    def go_detailPage(self):
        global detail_back
        #self.hide()
        self.close()
        self.detailpage = DetailPage()
        print("go to detail page!")
        self.detailpage.exec_()
        if(detail_back == 1):
            detail_back =0
            self.show()

    def exit_program(self):
        print("Bye! - main")
        self.close()

    def clock(self):
        self.now = datetime.now()
        print(self.now)



class DetailPage(QDialog, QWidget, Ui_DetailUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("HI I'm Detail Page")
        #self.show()

    def main(self):
        pass

    def go_mainpage(self):
        global detail_back
        print("Bye! - detail")
        #self.main = MainPage()
        print("go to main page!")
        detail_back = 1
        self.close()
        #self.main.exec_()



class OtpPage(QDialog, QWidget, Ui_Otp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def check_otp(self):
        global success_acc
        self.otp_code = self.text_otp.toPlainText()
        print(self.otp_code)
        self.flag=0
        if(len(self.otp_code) == 6):
            self.flag = 1
            self.cur = db.cursor()

            self.sql_str = "select * from test where otp=" + self.otp_code
            self.cur.execute(self.sql_str)
            if(self.cur.rowcount ==1):
                for(id,name,otp) in self.cur:
                    print(id, name, otp)
                    self.plant_id = id
                    self.name = name
                self.flag = 1
                self.sql_str = "update test set otp = NULL where otp=" + self.otp_code
                self.cur.execute(self.sql_str)
                db.commit()

                #json 수정
               # with open("./user_setting.json","w")
            else:
                self.flag = 0

        #성공했을때_db에 정보존재
        if(self.flag == 1):
            success_acc = 1
            self.close()
        else:
            #실패했을때
            msgBox = QMessageBox()
            msgBox.setText("Wrong OTP")
            msgBox.exec()
            success_acc = 0
            self.text_otp.clear()



    def back_entry(self):
        #메인으로 다시 돌아감
        self.close()


app=QApplication()
main = EntryPage()
success_acc = 0
detail_back =0
widget = QStackedWidget()

#widget.addWidget()



main.show()
app.exec_()
