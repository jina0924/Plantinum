from PySide2.QtWidgets import *
from PySide2.QtCore import *
from entryUI import Ui_Form as Ui_EntryUI
from mainUI import Ui_Form as Ui_MainUI
from detailUI import Ui_Form as Ui_DetailUI
from otpUI import Ui_Form as Ui_Otp
from sleepUI import Ui_Form as Ui_SleepUI

import mysql.connector
import json
from datetime import datetime
import time
import sys


#variable
success_acc = 0
detail_back =0
otp_back = 0

userfilepath= "./user_setting.json"
plant_id = -1

#물임계점
water_point = -1
#물통 양 디지털
water_amount = 0
#recnet_watering의 크기
watering_cnt=0
temp=0
humi=0
#파도 움직임
waveLV = 120
#취침모드
issleep=0


#페이지 생성 확인용
is_detail_page = 0
is_sleep_page = 0

#센서 측정 스레드_메인시작시 같이 시작
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

                #print("A :",a)
                #a += 1
                #센서측정
                temp += 1
                humi += 1

                #특정주기 센서
                if(a>100):
                    a=0

                #파도 수위 변경
                if (a% 5 ==0 ):
                    #waveLV = a*6 + 150
                    watering()
                time.sleep(1)


#물줄때
def watering():
    global watering_cnt
    user_data['recent_watering'].append(datetime.now().strftime("%y.%m.%d %H:%M"));
    watering_cnt += 1
    if(watering_cnt > 3):
        del(user_data['recent_watering'][0])
        watering_cnt = 3
    print(*user_data['recent_watering'])

    with open(userfilepath, "w", encoding='utf-8') as file:
        json.dump(user_data, file, indent="\t",ensure_ascii=False)


#시작페이지
class EntryPage(QDialog, QWidget, Ui_EntryUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dbset()

    def dbset(self):
        #db커넥트
        global db
        db = mysql.connector.connect(host="192.168.45.220",user='root', password='111111', database='testdb',buffered=True)

    def main(self):
        pass

    #새식물 등록
    def new_plant(self):

        widget.setCurrentIndex(1)

    def old_plant(self):
        global success_acc
        global plant_id,nickname,water_amount
        global user_data,watering_cnt

        #쿼리요청
        self.cur = db.cursor()
        self.sql_str = "select isconnect from test where id=" + str(user_data['id'])
        self.cur.execute(self.sql_str)

        for result in self.cur:
            # connect success 바로 메인페이지로 이동
            if(result[0] == 1):
                #connect == 1 이면 연결유지 상태 메인페이지 이동
                print("go to main page!")
                success_acc = 1
                widget.addWidget(MainPage())
                widget.setCurrentIndex(2)
            else:
                #연결이 끊기면 오류메세지
                msgBox = QMessageBox()
                msgBox.setText("There are no connected plants")
                msgBox.exec()
                #연결이 끊겨있으므로 user_data정보 지워줌

                user_data['id'] = -1
                user_data['nickname'] = ""
                user_data['water_point'] = -1
                user_data['recent_watering']= []

                # 수정반영
                with open(userfilepath, "w", encoding='utf-8') as file:
                    json.dump(user_data, file, indent="\t", ensure_ascii=False)

            #print(result[0])

        #다시 누를 것 대비_변경반영
        db.commit()

#메인 페이지 _ 파도 화면
class MainPage(QDialog, QWidget, Ui_MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("HI I'm MainPage")
        #시계를 위해 5초에 한번 화면 새로고침


        self.main()

    def main(self):
        global snsth, clock_timer
        self.warn_label.hide()

        #시계 타이머
        clock_timer = QTimer(self)
        clock_timer.setInterval(1000)  # 1초 => 나중에 5초에 한번으로 바꿀거임
        clock_timer.timeout.connect(self.show_clock)
        clock_timer.start()

        #센서 스레드
        snsth = sensorThread()
        snsth.start()

    def go_detailPage(self):
        global detail_back,is_detail_page
        #화면 새로고침 필요없음
        clock_timer.stop()
        #디테일페이지 선언 및 화면 전환
        if (is_detail_page == 0):
            is_detail_page == 1
            widget.addWidget(DetailPage())

        widget.setCurrentIndex(3)
        # 뒤로가기 버튼으로 돌아왔을때
        '''
        if(detail_back == 1):
            detail_back =0
            #self.timer.start()
        '''

#    def exit_program(self):
 #       print("Bye! - main")
  #      self.close()
    #화면 새로고침
    def show_clock(self):
        global now_time
        #시간 00:00 형태
        self.now = datetime.now().strftime('%H : %M')
        #now_time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        self.clock.setText(self.now)
        #온습도 글씨
        self.humi_label.setText(str(humi)+"%")
        self.temp_label.setText(str(temp)+"ºC")

        #파도 조절
        self.wave.setGeometry(QRect(0, waveLV , 1366, 768))
        #print(now_time)





class DetailPage(QDialog, QWidget, Ui_DetailUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("HI I'm Detail Page")
        #최근 관수날짜 보드
        #초기화 후 채워넣음
        self.watering_board = [self.label_8, self.label_9, self.label_10]
        self.label_8.clear()
        self.label_9.clear()
        self.label_10.clear()
        self.label_11.setText(user_data['nickname'])
        #화면 새로고침 한번 하고 시작
        self.redo()
        #self.main()

    def main(self):
       #self.testlabel.setText(str(a))
       pass
    #메인페이지로 돌아감
    def go_mainpage(self):
        '''
        global detail_back
        print("Bye! - detail")
        #self.main = MainPage()
        print("go to main page!")
        detail_back = 1
        self.close()
        #self.main.exec_()
        '''
        global clock_timer
        widget.setCurrentIndex(2)
        clock_timer.start()
    #취침모드
    def sleep_mode(self):
        global issleep,is_sleep_page

        issleep = 1
        '''
        self.close()
        self.sleeppage = SleepPage()
        print("go to sleep page!")
        self.sleeppage.exec_()
        issleep=0
        '''
        #취침모드에서 벗어나면 바로 메인페이지로 돌아감
        #self.go_mainpage()
        if(is_sleep_page == 0):
            is_sleep_page = 1
            widget.addWidget(SleepPage())

        widget.setCurrentIndex(4)

    #새로고침
    def redo(self):
        print("redo!!")
        #관수정보
        for i in range(len(user_data['recent_watering'])):
            self.watering_board[i].setText(user_data['recent_watering'][len(user_data['recent_watering'])-i-1])

        #닉네임
        self.cur = db.cursor()
        self.sql_str = "select name from test where id=" + str(user_data['id'])
        self.cur.execute(self.sql_str)

        for (res) in self.cur:
            #print(res)
            #닉네임 변경시
            if(res[0] != user_data['nickname']):
                self.label_11.setText(res[0])
                user_data['nickname'] = res[0]
                with open(userfilepath, "w", encoding='utf-8') as file:
                    json.dump(user_data, file, indent="\t", ensure_ascii=False)

        self.cur.close()
        db.commit()

        #물의 양
        if(water_amount == 1):
            self.progressBar.setStyleSheet(
                "QProgressBar::chunk { background-color : rgb(163, 77, 79) ; border-radius : 10px;} QProgressBar {background-color : rgb(255,255,255);border-radius : 15px;}")
            self.progressBar.setValue(80)
        else:
            self.progressBar.setStyleSheet(
                "QProgressBar::chunk { background-color : rgb(101, 128, 93) ; border-radius : 10px;} QProgressBar {background-color : rgb(255,255,255);border-radius : 15px;}")
            self.progressBar.setValue(40)
    #프로그램 및 라즈베리파이 종료
    #코드 해제를 위함
    def turnoff(self):
        global clock_timer, snsth
        clock_timer.stop()
        snsth.stop()
        quit()
        #라즈베리파이 종료 필요
        #배쉬파일 연결해야할듯 합니다
        sys.exit(0)


#otp코드
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

        #otp코드가 6자리일때
        if(len(self.otp_code) == 6):
            #self.flag = 1
            self.cur = db.cursor()

            # is otp exist?
            self.sql_str = "select * from test where otp=" + self.otp_code
            self.cur.execute(self.sql_str)
            # result = 1개
            if(self.cur.rowcount ==1):
                #id, 닉네임, 물의 양 등 저장
                for(id,name,otp,isconnect) in self.cur:
                    print(id, name, otp, isconnect)
                    #Already connect
                    #이미 연결이 되어있는 식물의 경우
                    if(isconnect == 1):
                        self.flag = 2
                        break;
                    #가져온 id(pk),name 저장
                    self.plant_id = int(id)
                    self.name = str(name)

                # Success connect!
                if(self.flag != 2):
                    self.flag = 1

                    # make otp=NULL, isconnect = 1
                    self.sql_str = "update test set otp = NULL, isconnect = 1 where otp=" + self.otp_code
                    self.cur.execute(self.sql_str)

                    #json 수정



#                    print(self.user_data['id'], self.user_data['nickname']
                    user_data['id'] = self.plant_id
                    user_data['nickname'] = self.name
                    user_data['recent_watering'] = []

                    #수정반영
                    with open(userfilepath, "w", encoding='utf-8') as file:
                        json.dump(user_data, file, indent="\t",ensure_ascii=False)

                    plant_id = self.plant_id
                    water_amount = 0

                    db.commit()
            else:
                self.flag = 0

        #성공했을때_db에 정보존재
        if(self.flag == 1):
            success_acc = 1
            widget.addWidget(MainPage())
            widget.setCurrentIndex(2)
        else:
            #실패했을때
            msgBox = QMessageBox()
            if(self.flag == 2):
                msgBox.setText("Already connected")
            else:
                msgBox.setText("Wrong OTP")
            msgBox.exec()

            #실패시 otp코드 초기화
            success_acc = 0
            for i in range(6):
                self.number_label[i].clear()
            self.otp_code = ""



    def back_entry(self):
        #global otp_back
        #메인으로 다시 돌아감
        #otp_back = 1
        #self.close()
        widget.setCurrentIndex(0)

    #숫자보드 입력
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


#취침 화면
class SleepPage(QDialog, QWidget, Ui_SleepUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("HI I'm Sleep Page")
        #self.show()
        #self.main()

    def main(self):
       #self.testlabel.setText(str(a))
       #ScreenSaver
       pass

    #화면 터치시 취침모드 종료 후 파도화면으로 돌아감
    def wakeup(self):
        #self.close()
        clock_timer.start()
        widget.setCurrentIndex(2)


app=QApplication()
main = EntryPage()

widget = QStackedWidget()
widget.addWidget(main)
widget.addWidget(OtpPage())
widget.setFixedHeight(768)
widget.setFixedWidth(1366)
#프로그램 실행 전 user_data 불러옴
#한글 읽기 위하여 encoding 표시
with open(userfilepath, "r", encoding="utf-8") as file:
    user_data = json.load(file)

widget.show()
app.exec_()
