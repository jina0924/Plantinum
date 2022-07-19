from PySide6.QtWidgets import *
from entry import Ui_MainWindow
from mainUI import Ui_Form as Ui_MainUI
from detailUI import Ui_Form as Ui_DetailUI


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def main(self):
        pass

    def new_plant(self):
        print("regist new plant!")

    def old_plant(self):
        self.hide()
        print("go to main page!")
        self.second = MainPage()
        self.second.exec_()
        #self.close()


class MainPage(QWidget, Ui_MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("HI I'm MainPage")
        self.show()

    def main(self):
        pass

    def go_detailPage(self):
        self.hide()
        self.second = DetailPage()
        print("go to detail page!")
        self.second.exec()
        self.show()
        self.exec()

    def exit_program(self):
        print(" Bye! - main")
        self.close()


class DetailPage(QWidget, Ui_DetailUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("HI I'm Detail Page")
        self.show()

    def main(self):
        pass

    def go_mainpage(self):
        print("Bye! - detail")
        self.close()



app=QApplication()
main = MyApp()

main.show()
app.exec_()