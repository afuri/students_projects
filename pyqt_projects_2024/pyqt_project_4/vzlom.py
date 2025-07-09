import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from simon import Simon
from question_wd import Question_Window
from db_show import Database_Show
from PyQt5.Qt import QDateTime


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.hel = Hello_window()
        self.w1 = First_window()
        self.df_ch = Difficult_choice()
        self.qu = Question_Window()
        self.db_s = Database_Show()

    def show_hellow_wd(self):      # start window
        self.hel.show()
        self.hel.next_bt.clicked.connect(self.hellow_to_question)

    def hellow_to_question(self):
        with open('logi', mode='a+', encoding='utf8') as file:
            file.write(f"Запуск программы {QDateTime.currentDateTime().toString('yyyy.MM.dd hh:mm:ss, dddd')}\n")
        self.qu.show()
        self.qu.pushb_no.clicked.connect(self.show_window_1)
        self.qu.pushb_no.clicked.connect(lambda: self.qu.hide())
        self.qu.pushb_yes.clicked.connect(self.database_show_func)

    def database_show_func(self):
        self.qu.hide()
        self.db_s.show()
        self.db_s.back_bt.clicked.connect(self.back_function)

    def back_function(self):
        self.qu.show()
        self.db_s.hide()

    def show_window_1(self):
        self.w1.show()
        self.w1.pushButton_cancel.clicked.connect(lambda: self.qu.show())
        self.w1.pushButton_ok.clicked.connect(self.w1.close)
        self.w1.pushButton_ok.clicked.connect(self.show_window_choice)

    def show_window_choice(self):
        self.df_ch.show()
        self.df_ch.level1_bt.clicked.connect(self.send)
        self.df_ch.level2_bt.clicked.connect(self.send)
        self.df_ch.level3_bt.clicked.connect(self.send)

    def send(self):
        send = self.sender()
        self.s_t = send.text()
        sim = Simon(self.s_t)
        sim.show()
        self.df_ch.close()


class Hello_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Hello_window, self).__init__()
        uic.loadUi('uic/hello_window.ui', self)
        self.setWindowIcon(QtGui.QIcon('images/hand.png'))
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.close_bt.setIcon(QtGui.QIcon('images/close.png'))
        self.close_bt.setIconSize(QtCore.QSize(20, 20))
        self.close_bt.clicked.connect(lambda: sys.exit(app.exec_()))

        self.fon_lb_helwd.setPixmap(QtGui.QPixmap('images/fon1.jpg'))

        self.svor_bt.setIcon(QtGui.QIcon('images/svor.png'))
        self.svor_bt.setIconSize(QtCore.QSize(20, 20))
        self.svor_bt.clicked.connect(lambda: self.showMinimized())
        self.next_bt.clicked.connect(self.close)


class First_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(First_window, self).__init__()
        uic.loadUi('uic/first_window.ui', self)
        self.setWindowIcon(QtGui.QIcon('images/warning.png'))

        self.pushButton_cancel.clicked.connect(lambda: self.hide())


class Difficult_choice(QtWidgets.QWidget):
    def __init__(self):
        super(Difficult_choice, self).__init__()
        uic.loadUi('uic/difficult_choice.ui', self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.hide()
    w.show_hellow_wd()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
