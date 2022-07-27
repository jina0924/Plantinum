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
userfilepath= "./user_setting.json"
plant_id = -1
water_point = -1
watering_cnt=0
temp=0
humi=0
waveLV = 500

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
        global a,temp,humi,waveLV
        print("start thread")
        a = 1
        while(1):
            if(success_acc == 0):
                continue
            else:
                #code, code

                print("A :",a)
                a += 1
                temp += 1
                humi += 1
                if(a>100):
                    a=0

                if ( a% 5 ==0 ):
                    #waveLV = a*6 + 150
                    watering()
                time.sleep(1)


def watering():
    global watering_cnt
    user_data['recent_watering'].append(datetime.now().strftime("%y.%m.%d %H:%M"));
    watering_cnt += 1
    if(watering_cnt > 3):
        del(user_data['recent_watering'][0])
        watering_cnt = 3
    print(*user_data['recent_watering'])

    with open(userfilepath, "w", encoding='utf-8') as file:
        json.dump(user_data, file, indent="\t")


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
        global plant_id,nickname,water_amount
        global user_data,watering_cnt



        #connect test
        with open(userfilepath, "r") as file:
            user_data = json.load(file)

        self.cur = db.cursor()
        self.sql_str = "select isconnect from test where id=" + str(user_data['id'])
        self.cur.execute(self.sql_str)

        for result in self.cur:
            # connect success 바로 메인페이지로 이동
            if(result[0] == 1):
                self.hide()
                print("go to main page!")
                self.second = MainPage()
                success_acc = 1
                watering_cnt = len(user_data['recent_watering'])
                self.second.show()
            else:
                msgBox = QMessageBox()
                msgBox.setText("There are no connected plants")
                msgBox.exec()

            print(result[0])


#        self.second.exec_()
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

        self.warn_label.hide()

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
        now = datetime.now().strftime('%H : %M')
        #now_time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        self.clock.setText(now)
        self.waterLV_label.setText(str(humi))
        self.temp_label.setText(str(temp))

        self.wave.setGeometry(QRect(0, waveLV , 1024, 600))
        #print(now_time)





class DetailPage(QDialog, QWidget, Ui_DetailUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("HI I'm Detail Page")
        #self.show()
        self.label_8.clear()
        self.label_9.clear()
        self.label_10.clear()
        self.main()

    def main(self):
       #self.testlabel.setText(str(a))
       pass

    def go_mainpage(self):
        global detail_back
        print("Bye! - detail")
        #self.main = MainPage()
        print("go to main page!")
        detail_back = 1
        self.close()
        #self.main.exec_()

    def sleep_mode(self):
        self.redo()
        pass

    def redo(self):
        print("redo!!")
        self.watering_board = [self.label_10,self.label_9,self.label_8]

        for i in range(len(user_data['recent_watering'])):
            self.watering_board[i].setText(user_data['recent_watering'][i]);

        pass

    def turnoff(self):
        pass



class OtpPage(QDialog, QWidget, Ui_Otp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.otp_code = ""
        self.number_label = [self.number_1, self.number_2, self.number_3, self.number_4, self.number_5, self.number_6]
        for i in range(6):
            self.number_label[i].clear()


    def check_otp(self):
        global success_acc
        global plant_id, water_amount
        print(self.otp_code)
        self.flag=0

        if(len(self.otp_code) == 6):
            #self.flag = 1
            self.cur = db.cursor()

            # is otp exist?
            self.sql_str = "select * from test where otp=" + self.otp_code
            self.cur.execute(self.sql_str)
            # result = 1개
            if(self.cur.rowcount ==1):
                #id, 닉네임, 물의 양 저장
                for(id,name,otp,isconnect) in self.cur:
                    print(id, name, otp, isconnect)
                    #Already connect
                    if(isconnect == 1):
                        self.flag = 2
                        break;
                    self.plant_id = int(id)
                    self.name = str(name)

                # Success connect!
                if(self.flag != 2):
                    self.flag = 1

                    # make otp=NULL, isconnect = 1
                    self.sql_str = "update test set otp = "", isconnect = 1 where otp=" + self.otp_code
                    self.cur.execute(self.sql_str)

                    #json 수정

                    with open(userfilepath, "r") as file:
                        user_data = json.load(file)


#                    print(self.user_data['id'], self.user_data['nickname'], self.user_data['water_amount'])
                    user_data['id'] = self.plant_id
                    user_data['water_amount'] = 80
                    user_data['recent_watering'] = []

                    with open(userfilepath, "w", encoding='utf-8') as file:
                        json.dump(user_data, file, indent="\t")

                    plant_id = self.plant_id
                    water_amount = 80

                    db.commit()
            else:
                self.flag = 0

        #성공했을때_db에 정보존재
        if(self.flag == 1):
            success_acc = 1
            self.close()
        else:
            #실패했을때
            msgBox = QMessageBox()
            if(self.flag == 2):
                msgBox.setText("Already connected")
            else:
                msgBox.setText("Wrong OTP")
            msgBox.exec()


            success_acc = 0
            for i in range(6):
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
            if(len(self.otp_code) < 6):
                self.otp_code += self.send
                self.number_label[len(self.otp_code)-1].setText(self.send)




app=QApplication()
main = EntryPage()

#widget = QStackedWidget()

main.show()
app.exec_()
