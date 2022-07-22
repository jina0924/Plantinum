from PySide6.QtWidgets import *
from PySide6.QtCore import *
from entry import Ui_MainWindow
from entryUI import Ui_Form as Ui_EntryUI
from mainUI import Ui_Form as Ui_MainUI
from detailUI import Ui_Form as Ui_DetailUI
from otpUI import Ui_Form as Ui_Otp

import mysql.connector
import json
from datetime import datetime
import time


#variable
success_acc = 0
detail_back =0
otp_back = 0

class sensorThread(QThread):
    global a,success_acc

    def __init__(self):
        super().__init__()
        print("make thread")

    def stop(self):
        self.quit()
        self.wait(1000)
        print("stop thread")

    def run(self):
        global a
        print("start thread")
        a = 1
        while(1):
            if(success_acc == 0):
                continue
            else:
                #code, code

                print("A :",a)
                a += 1
                time.sleep(1)



class EntryPage(QMainWindow, Ui_EntryUI):
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
        global otp_back
        #otp 등록페이지로 이동
        self.hide()
        print("regist new plant!")
        self.go_otp = OtpPage()
        self.go_otp.exec_()
        if(success_acc == 1):
            self.old_plant()
        elif (otp_back == 1):
            otp_back = 0
            self.show()

    def old_plant(self):
        global success_acc
        #바로 메인페이지로 이동
        self.hide()
        print("go to main page!")
        self.second = MainPage()
        success_acc =1
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
        #now_timer.start()
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 1초 => 나중에 5초에 한번으로 바꿀거임
        self.timer.timeout.connect(self.show_clock)
        self.timer.start()

        self.snsth = sensorThread()
        self.snsth.start()



    def main(self):
       pass

    def go_detailPage(self):
        global detail_back
        #self.hide()
        self.close()
        self.timer.stop()
        self.detailpage = DetailPage()
        print("go to detail page!")
        self.detailpage.exec_()
        if(detail_back == 1):
            detail_back =0
            self.show()
            self.timer.start()

    def exit_program(self):
        print("Bye! - main")
        self.close()

    def show_clock(self):
        global now_time
        now = datetime.now()
        now_time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        self.clock.setText(now_time)
        print(now_time)




class DetailPage(QDialog, QWidget, Ui_DetailUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("HI I'm Detail Page")
        #self.show()
        self.main()

    def main(self):
       self.testlabel.setText(str(a))
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
        self.otp_code = ""
        self.number_label = [self.number_1, self.number_2, self.number_3, self.number_4]
        for i in range(4):
            self.number_label[i].clear()


    def check_otp(self):
        global success_acc
        print(self.otp_code)
        self.flag=0
        if(len(self.otp_code) == 4):
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
            for i in range(4):
                self.number_label[i].clear()
            self.otp_code = ""



    def back_entry(self):
        global otp_back
        #메인으로 다시 돌아감
        otp_back = 1
        self.close()

    def click_pad(self):
        self.send = self.sender().text()
        print(self.send)


        if( self.send == "<"):
            if(len(self.otp_code) != 0):
                self.number_label[len(self.otp_code) - 1].clear()
                self.otp_code = self.otp_code[:-1]

            print("back space")
        else:
            if(len(self.otp_code) != 4):
                self.otp_code += self.send
                self.number_label[len(self.otp_code)-1].setText(self.send)




app=QApplication()
main = EntryPage()

#widget = QStackedWidget()

main.show()
app.exec_()
