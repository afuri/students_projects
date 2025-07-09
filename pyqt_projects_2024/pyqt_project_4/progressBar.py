import random
import time
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt
from reg import Registration_Window


class ProgressHandler(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(list)

    def run(self):
        for i in range(101):
            self.my_signal.emit(['progress_step', i])
            time.sleep(0.05)


class Progress(QtWidgets.QWidget):
    def __init__(self, fin=''):
        super(Progress, self).__init__()
        uic.loadUi('uic/wid.ui', self)
        self.pushButton_2.hide()
        self.fin = fin
        self.w2 = Second_window()

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def signal_handler(self, value):
        final_value = self.fin
        fake_text_list = [
            'Установка пакетов...',
            "Загрузка данных...",
            "Обработка данных...",
            "Синхронизация с сервером...",
            "Идентификация потоков...",
            "Создание активной сессии..."
        ]

        if value[1] == final_value:
            self.label_2.setText('Процесс завершен')
            self.show_window2()

        if value[0] == 'progress_step':
            current_value = self.progressBar.value()
            self.progressBar.setValue(current_value + 1)

            if value[1] % 25 == 0:
                random_data = random.choice(fake_text_list)
                self.label_2.setText(random_data)

    def show_window2(self):
        self.w2.show()
        good = f'Поздравляем! Вы взломали Пентагон на {self.fin}%!'
        self.w2.show_good(good, f'{self.fin}%')
        self.hide()


class Second_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Second_window, self).__init__()
        uic.loadUi('uic/second_window.ui', self)
        self.textBrowser_bad.hide()
        self.textBrowser_good.hide()
        self.happy_smile_lb1.hide(), self.happy_smile_lb2.hide()
        self.sad_smile_lb1.hide(), self.sad_smile_lb2.hide()

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

    def show_bad(self):
        self.pushButton_cancel.clicked.connect(lambda: exit())
        self.textBrowser_bad.show()
        self.sad_smile_lb1.show(), self.sad_smile_lb2.show()

    def show_good(self, text='', f=''):
        self.reg_wd = Registration_Window(f)
        self.textBrowser_good.show()
        self.textBrowser_good.setText(text)
        self.textBrowser_good.setStyleSheet('color: rgb(255, 255, 255);\nfont: 18pt "MS Shell Dlg 2";')
        self.textBrowser_good.setAlignment(Qt.AlignCenter)
        self.happy_smile_lb1.show(), self.happy_smile_lb2.show()
        self.pushButton_cancel.setText('Далее')
        self.pushButton_cancel.setStyleSheet('color: rgb(255, 255, 255);\nbackground-color: rgb(63, 191, 0);')
        self.pushButton_cancel.clicked.connect(self.wd2_to_reg)

    def wd2_to_reg(self):
        self.hide()
        self.reg_wd.show()


class Lite_Mode_Window(QtWidgets.QWidget):
    def __init__(self):
        super(Lite_Mode_Window, self).__init__()
        uic.loadUi('uic/lite_w2.ui', self)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.pushButton_next.clicked.connect(self.wd2_to_reg)

    def show_good_lite(self, text='', f=''):
        self.reg_wd = Registration_Window(f)
        self.textBrowser_good.setText(text)
        self.textBrowser_good.setAlignment(Qt.AlignCenter)

    def wd2_to_reg(self):
        self.hide()
        self.reg_wd.show()
