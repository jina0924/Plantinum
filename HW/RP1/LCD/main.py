from PySide6.QtWidgets import *
from entry import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def main(self):
        pass

    def new_plant(self):
        print("regist new plant!")

    def old_plant(self):
        print("go to main page!")


app=QApplication()
main = MyApp()

main.show()
app.exec()