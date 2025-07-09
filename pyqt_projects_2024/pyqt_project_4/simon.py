from PyQt5 import uic
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QMainWindow
from random import randint
from progressBar import Progress, ProgressHandler, Second_window, Lite_Mode_Window


class Simon(QMainWindow):
    def __init__(self, num):
        super().__init__()
        self.b9, self.b16 = False, False
        self.num = num
        self.FINAL_VALUE_DICT = {'•': 50, '••': 75, '•••': 100}
        self.fin = self.FINAL_VALUE_DICT[num]
        self.handler = ProgressHandler()
        self.pr = Progress(self.FINAL_VALUE_DICT[num])
        self.w2 = Second_window()
        self.w2_lite = Lite_Mode_Window()
        try:
            if num == '•':
                uic.loadUi('uic/simon_2x2.ui', self)
                self.sch, self.fin_val = 1, 50
            elif num == '••':
                uic.loadUi('uic/simon_3x3.ui', self)
                self.b9 = True
                self.sch, self.fin_val = 2, 75
            elif num == '•••':
                uic.loadUi('uic/simon_4x4.ui', self)
                self.b9 = True
                self.b16 = True
                self.sch, self.fin_val = 3, 100
            else:
                exit()
        except:
            exit()
        self.start_bt.clicked.connect(self.start)
        self.start_bt.clicked.connect(lambda: self.start_bt.hide())
        self.BUTTONS = {1: 'pushButton_1', 2: 'pushButton_2', 3: 'pushButton_3',
                        4: 'pushButton_4', 5: 'pushButton_5', 6: 'pushButton_6',
                        7: 'pushButton_7', 8: 'pushButton_8', 9: 'pushButton_9',
                        10: 'pushButton_10', 11: 'pushButton_11', 12: 'pushButton_12',
                        13: 'pushButton_13', 14: 'pushButton_14', 15: 'pushButton_15',
                        16: 'pushButton_16'}
        self.DIFFICULT = {1: 4, 2: 9, 3: 16}
        self.DICT_COUNT = {1: 4, 2: 6, 3: 6}
        self.timer = QTimer()
        self.timer.timeout.connect(self.process)
        self.your_lb.hide()
        self.subsequence = []

        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

    def start(self):
        self.count = 1
        self.timer.start(1000)

    def setblack(self):
        self.pushButton_1.setStyleSheet('background-color: rgb(20, 20, 20);')
        self.pushButton_2.setStyleSheet('background-color: rgb(20, 20, 20);')
        self.pushButton_3.setStyleSheet('background-color: rgb(20, 20, 20);')
        self.pushButton_4.setStyleSheet('background-color: rgb(20, 20, 20);')
        if self.b9:
            self.pushButton_5.setStyleSheet('background-color: rgb(20, 20, 20);')
            self.pushButton_6.setStyleSheet('background-color: rgb(20, 20, 20);')
            self.pushButton_7.setStyleSheet('background-color: rgb(20, 20, 20);')
            self.pushButton_8.setStyleSheet('background-color: rgb(20, 20, 20);')
            self.pushButton_9.setStyleSheet('background-color: rgb(20, 20, 20);')
        if self.b16:
            self.pushButton_10.setStyleSheet('background-color: rgb(20, 20, 20);')
            self.pushButton_11.setStyleSheet('background-color: rgb(20, 20, 20);')
            self.pushButton_12.setStyleSheet('background-color: rgb(20, 20, 20);')
            self.pushButton_13.setStyleSheet('background-color: rgb(20, 20, 20);')
            self.pushButton_14.setStyleSheet('background-color: rgb(20, 20, 20);')
            self.pushButton_15.setStyleSheet('background-color: rgb(20, 20, 20);')
            self.pushButton_16.setStyleSheet('background-color: rgb(20, 20, 20);')

    def setgreen(self):
        self.pushButton_1.setStyleSheet('background-color: rgb(82,249,21);')
        self.pushButton_2.setStyleSheet('background-color: rgb(82,249,21);')
        self.pushButton_3.setStyleSheet('background-color: rgb(82,249,21);')
        self.pushButton_4.setStyleSheet('background-color: rgb(82,249,21);')
        if self.b9:
            self.pushButton_5.setStyleSheet('background-color: rgb(82,249,21);')
            self.pushButton_6.setStyleSheet('background-color: rgb(82,249,21);')
            self.pushButton_7.setStyleSheet('background-color: rgb(82,249,21);')
            self.pushButton_8.setStyleSheet('background-color: rgb(82,249,21);')
            self.pushButton_9.setStyleSheet('background-color: rgb(82,249,21);')
        if self.b16:
            self.pushButton_10.setStyleSheet('background-color: rgb(82,249,21);')
            self.pushButton_11.setStyleSheet('background-color: rgb(82,249,21);')
            self.pushButton_12.setStyleSheet('background-color: rgb(82,249,21);')
            self.pushButton_13.setStyleSheet('background-color: rgb(82,249,21);')
            self.pushButton_14.setStyleSheet('background-color: rgb(82,249,21);')
            self.pushButton_15.setStyleSheet('background-color: rgb(82,249,21);')
            self.pushButton_16.setStyleSheet('background-color: rgb(82,249,21);')

    def setred(self):
        self.pushButton_1.setStyleSheet('background-color: rgb(254,0,0);')
        self.pushButton_2.setStyleSheet('background-color: rgb(254,0,0);')
        self.pushButton_3.setStyleSheet('background-color: rgb(254,0,0);')
        self.pushButton_4.setStyleSheet('background-color: rgb(254,0,0);')
        if self.b9:
            self.pushButton_5.setStyleSheet('background-color: rgb(254,0,0);')
            self.pushButton_6.setStyleSheet('background-color: rgb(254,0,0);')
            self.pushButton_7.setStyleSheet('background-color: rgb(254,0,0);')
            self.pushButton_8.setStyleSheet('background-color: rgb(254,0,0);')
            self.pushButton_9.setStyleSheet('background-color: rgb(254,0,0);')
        if self.b16:
            self.pushButton_10.setStyleSheet('background-color: rgb(254,0,0);')
            self.pushButton_11.setStyleSheet('background-color: rgb(254,0,0);')
            self.pushButton_12.setStyleSheet('background-color: rgb(254,0,0);')
            self.pushButton_13.setStyleSheet('background-color: rgb(254,0,0);')
            self.pushButton_14.setStyleSheet('background-color: rgb(254,0,0);')
            self.pushButton_15.setStyleSheet('background-color: rgb(254,0,0);')
            self.pushButton_16.setStyleSheet('background-color: rgb(254,0,0);')

    def enable(self):
        self.pushButton_1.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        if self.b9:
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(False)
            self.pushButton_7.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.pushButton_9.setEnabled(False)
        if self.b16:
            self.pushButton_10.setEnabled(False)
            self.pushButton_11.setEnabled(False)
            self.pushButton_12.setEnabled(False)
            self.pushButton_13.setEnabled(False)
            self.pushButton_14.setEnabled(False)
            self.pushButton_15.setEnabled(False)
            self.pushButton_16.setEnabled(False)

    def set_bt(self, vvod, fl=False):
        if vvod == 'pushButton_1':
            self.bt = self.pushButton_1
            if fl:
                self.subsequence.append('pushButton_1')
        elif vvod == 'pushButton_2':
            self.bt = self.pushButton_2
            if fl:
                self.subsequence.append('pushButton_2')
        elif vvod == 'pushButton_3':
            self.bt = self.pushButton_3
            if fl:
                self.subsequence.append('pushButton_3')
        elif vvod == 'pushButton_4':
            self.bt = self.pushButton_4
            if fl:
                self.subsequence.append('pushButton_4')
        elif vvod == 'pushButton_5':
            self.bt = self.pushButton_5
            if fl:
                self.subsequence.append('pushButton_5')
        elif vvod == 'pushButton_6':
            self.bt = self.pushButton_6
            if fl:
                self.subsequence.append('pushButton_6')
        elif vvod == 'pushButton_7':
            self.bt = self.pushButton_7
            if fl:
                self.subsequence.append('pushButton_7')
        elif vvod == 'pushButton_8':
            self.bt = self.pushButton_8
            if fl:
                self.subsequence.append('pushButton_8')
        elif vvod == 'pushButton_9':
            self.bt = self.pushButton_9
            if fl:
                self.subsequence.append('pushButton_9')
        elif vvod == 'pushButton_10':
            self.bt = self.pushButton_10
            if fl:
                self.subsequence.append('pushButton_10')
        elif vvod == 'pushButton_11':
            self.bt = self.pushButton_11
            if fl:
                self.subsequence.append('pushButton_11')
        elif vvod == 'pushButton_12':
            self.bt = self.pushButton_12
            if fl:
                self.subsequence.append('pushButton_12')
        elif vvod == 'pushButton_13':
            self.bt = self.pushButton_13
            if fl:
                self.subsequence.append('pushButton_13')
        elif vvod == 'pushButton_14':
            self.bt = self.pushButton_14
            if fl:
                self.subsequence.append('pushButton_14')
        elif vvod == 'pushButton_15':
            self.bt = self.pushButton_15
            if fl:
                self.subsequence.append('pushButton_15')
        elif vvod == 'pushButton_16':
            self.bt = self.pushButton_16
            if fl:
                self.subsequence.append('pushButton_16')

    def button_color(self, n):
        if self.count == 1:
            n.setStyleSheet('background-color: rgb(155, 50, 190);')
        elif self.count == 2:
            n.setStyleSheet('background-color: rgb(192, 1, 255);')
        elif self.count == 3:
            n.setStyleSheet('background-color: rgb(127, 0, 255);')
        elif self.count == 4:
            n.setStyleSheet('background-color: rgb(63, 0, 255);')
        elif self.count == 5:
            n.setStyleSheet('background-color: rgb(155, 50, 190);')
        elif self.count == 6:
            n.setStyleSheet('background-color: rgb(192, 1, 255);')
        elif self.count == 7:
            n.setStyleSheet('background-color: rgb(127, 0, 255);')
        elif self.count == 8:
            n.setStyleSheet('background-color: rgb(63, 0, 255);')

    def process(self):
        if self.count < self.DICT_COUNT[self.sch] + 1:
            self.setblack()

            n = randint(1, self.DIFFICULT[self.sch])
            print(self.BUTTONS[n])  # логи

            self.set_bt(self.BUTTONS[n], fl=True)
            self.button_color(self.bt)
            self.count += 1
        else:
            self.timer.stop()
            self.setblack()
            self.check()

    def check(self):
        self.your_lb.show()
        print(self.subsequence)  # логи
        self.count = 1
        self.pushButton_1.clicked.connect(self.button_Click)
        self.pushButton_2.clicked.connect(self.button_Click)
        self.pushButton_3.clicked.connect(self.button_Click)
        self.pushButton_4.clicked.connect(self.button_Click)
        if self.b9:
            self.pushButton_5.clicked.connect(self.button_Click)
            self.pushButton_6.clicked.connect(self.button_Click)
            self.pushButton_7.clicked.connect(self.button_Click)
            self.pushButton_8.clicked.connect(self.button_Click)
            self.pushButton_9.clicked.connect(self.button_Click)
        if self.b16:
            self.pushButton_10.clicked.connect(self.button_Click)
            self.pushButton_11.clicked.connect(self.button_Click)
            self.pushButton_12.clicked.connect(self.button_Click)
            self.pushButton_13.clicked.connect(self.button_Click)
            self.pushButton_14.clicked.connect(self.button_Click)
            self.pushButton_15.clicked.connect(self.button_Click)
            self.pushButton_16.clicked.connect(self.button_Click)

    def button_Click(self):
        self.setblack()
        self.bad = 'Вы не смогли взломать Пентагон...'
        self.good = f'Поздравляем! Вы взломали Пентагон на {self.fin}%!'

        sender = self.sender()
        if len(self.subsequence) > 1:
            if self.subsequence[0] == str(sender.objectName()):
                self.your_lb.setText(str(self.count))
                self.subsequence.pop(0)
                self.set_bt(sender.objectName())
                self.button_color(self.bt)
                self.count += 1
            else:
                self.your_lb.setText(str(self.count))
                self.setred()
                QTimer.singleShot(1000, self.continius_bad)

        else:
            if self.subsequence[0] == str(sender.objectName()):
                self.your_lb.setText(str('Верно!'))
                self.subsequence.pop(0)
                self.setgreen()
                self.enable()
                QTimer.singleShot(1600, self.continius_good)
            else:
                self.your_lb.setText(str(self.count))
                self.setred()
                self.enable()
                QTimer.singleShot(1000, self.continius_bad)

    def continius_bad(self):
        self.w2.show_bad()
        self.hide()
        self.w2.show()

    def continius_good(self):
        if self.fin == 50:
            self.hide()
            self.w2_lite.show()
            self.w2_lite.show_good_lite(self.good, f'{self.fin}%')
        else:
            self.hide()
            self.handler.my_signal.connect(self.pr.signal_handler)
            self.pr.show()
            self.pr.progressBar.setValue(0)
            self.handler.start()

