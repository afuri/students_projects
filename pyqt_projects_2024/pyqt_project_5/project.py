import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3


class LoginDB():
    def __init__(self, namedb):
        self.namedb = namedb
        self.db = sqlite3.connect(self.namedb)
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Users(login TEXT NOT NULL, password TEXT NOT NULL)')

    def save(self):
        self.db.commit()
        self.db.close()


class EventDB():
    def __init__(self, namedb):
        self.namedb = namedb
        self.db = sqlite3.connect(self.namedb)
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Events(login TEXT NOT NULL, name TEXT NOT NULL, desc TEXT NOT NULL,'
                            'date TEXT NOT NULL, time TEXT NOT NULL)')

    def save(self):
        self.db.commit()
        self.db.close()


class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)

        lay = QVBoxLayout(content)

        self.label = QLabel(content)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)

        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 100, 700, 450)
        self.setWindowTitle('Ваш Дневник Занятости')

        self.pixmap1 = QPixmap('background1.png')
        self.pixmap1 = self.pixmap1.scaled(700, 450)
        self.image1 = QLabel(self)
        self.image1.move(0, 0)
        self.image1.resize(700, 450)
        self.image1.setPixmap(self.pixmap1)

        self.greetings = QLabel('Приветствую Вас в Вашем дневнике!', self)
        self.greetings.setFont(QFont('Arial', 17))
        self.greetings.resize(600, 50)
        self.greetings.move(100, 30)

        self.UiComponents()

        self.login = QPushButton(self)
        self.login.move(100, 350)
        self.login.resize(150, 30)
        self.login.setText('Войти')
        self.login.clicked.connect(self.log)

        self.auth = QPushButton(self)
        self.auth.move(450, 350)
        self.auth.resize(150, 30)
        self.auth.setText('Авторизоваться')
        self.auth.clicked.connect(self.authorization)

    def authorization(self):
        self.au = Auth()
        self.au.show()

    def log(self):
        self.lo = Log_in()
        self.lo.show()

    def UiComponents(self):
        text = "Это программа является дневником для записи событий." \
               "Чтобы не держать всю информацию в голове и путаться в датах " \
               "я предлагаю Вам протестироовать мою программу! Это намного удобнее" \
               " бумажных дневников, ведь моя программа точно не затеряется среди " \
               " прочих книг!" \
               " \n" \
               " \n" \
               "Приятного пользования!"

        label = ScrollLabel(self)
        label.setText(text)
        label.setGeometry(200, 150, 300, 150)


class Log_in(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(650, 200, 400, 150)
        self.setWindowTitle('Вход')

        self.db1 = LoginDB('database.db')

        self.v1 = QLabel('Введите логин:', self)
        self.v1.move(10, 10)
        self.v1.setFont(QFont('Arial', 10))
        self.v1.resize(500, 50)

        self.line1 = QLineEdit(self)
        self.line1.move(140, 20)
        self.line1.resize(170, 30)
        self.line1.setStyleSheet('QLineEdit {background-color: #A3C1DA}')

        self.v2 = QLabel('Введите пароль:', self)
        self.v2.move(10, 50)
        self.v2.setFont(QFont('Arial', 10))
        self.v2.resize(500, 50)

        self.line2 = QLineEdit(self)
        self.line2.move(140, 60)
        self.line2.resize(170, 30)
        self.line2.setEchoMode(QLineEdit.Password)
        self.line2.setStyleSheet('QLineEdit {background-color: #A3C1DA}')

        self.buttonn = QPushButton(self)
        self.buttonn.move(120, 100)
        self.buttonn.resize(150, 30)
        self.buttonn.setText('Войти')
        self.buttonn.clicked.connect(self.exx)
        self.buttonn.setStyleSheet('QPushButton {background-color: #A3C1DA}')

    def exx(self):
        self.us_log = self.line1.text()
        self.us_pas = self.line2.text()
        result = self.db1.cursor.execute(f'SELECT * FROM Users').fetchall()
        result = {key: value for key, value in result}
        if self.us_log in result:
            if result[self.us_log] == self.us_pas:
                self.w = Diary(self.us_log, self)
                self.w.show()
                self.close()
            else:
                self.w = Np()
                self.w.show()
        else:
            self.w = Nl()
            self.w.show()


class Auth(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(650, 200, 400, 200)
        self.setWindowTitle('Авторизация')

        self.db1 = LoginDB('database.db')

        self.v1 = QLabel('Введите логин:', self)
        self.v1.move(10, 10)
        self.v1.setFont(QFont('Arial', 10))
        self.v1.resize(500, 50)

        self.line1 = QLineEdit(self)
        self.line1.move(140, 20)
        self.line1.resize(170, 30)
        self.line1.setStyleSheet('QLineEdit {background-color: #A3C1DA}')

        self.v2 = QLabel('Введите пароль:', self)
        self.v2.move(10, 50)
        self.v2.setFont(QFont('Arial', 10))
        self.v2.resize(500, 50)

        self.line2 = QLineEdit(self)
        self.line2.move(140, 60)
        self.line2.resize(170, 30)
        self.line2.setEchoMode(QLineEdit.Password)
        self.line2.setStyleSheet('QLineEdit {background-color: #A3C1DA}')

        self.v3 = QLabel('Повторите пароль:', self)
        self.v3.move(10, 90)
        self.v3.setFont(QFont('Arial', 10))
        self.v3.resize(500, 50)

        self.line3 = QLineEdit(self)
        self.line3.move(160, 100)
        self.line3.resize(170, 30)
        self.line3.setEchoMode(QLineEdit.Password)
        self.line3.setStyleSheet('QLineEdit {background-color: #A3C1DA}')

        self.buttonn = QPushButton(self)
        self.buttonn.move(120, 140)
        self.buttonn.resize(150, 30)
        self.buttonn.setText('Авторизоваться')
        self.buttonn.clicked.connect(self.exx)
        self.buttonn.setStyleSheet('QPushButton {background-color: #A3C1DA}')

    def exx(self):
        self.us_log = self.line1.text()
        self.us_pas1 = self.line2.text()
        self.us_pas2 = self.line3.text()
        if self.us_pas1 != self.us_pas2:
            self.w = Errorr()
            self.w.show()
        else:
            result = self.db1.cursor.execute(f'SELECT login FROM Users').fetchall()
            if (self.us_log,) not in result:
                self.db1.cursor.execute('INSERT INTO Users (login, password) VALUES (?, ?)',
                                        (str(self.us_log), str(self.us_pas1)))
                print('Пользователь зарегистрирован')
                self.db1.save()
                self.close()
            else:
                self.w = Errorr()
                self.w.show()


class Diary(QMainWindow):
    def __init__(self, login, parent=None):
        super(Diary, self).__init__(parent)
        self.initUI()
        self.login = login

    def initUI(self):
        self.setGeometry(550, 100, 750, 410)
        self.setWindowTitle('Ваш Дневник Занятости')

        self.db2 = EventDB('Events.db')

        self.pixmap2 = QPixmap('bckg.png')
        self.pixmap2 = self.pixmap2.scaled(750, 410)
        self.image2 = QLabel(self)
        self.image2.move(0, 0)
        self.image2.resize(750, 410)
        self.image2.setPixmap(self.pixmap2)

        self.new_event = QLabel('Создание нового события', self)
        self.new_event.move(0, 15)
        self.new_event.setFont(QFont('Arial', 13))
        self.new_event.resize(500, 50)

        self.t = QLabel('Выберите время', self)
        self.t.move(0, 60)
        self.t.setFont(QFont('Arial', 10))
        self.t.resize(500, 50)

        self.time = QTimeEdit(self)
        self.time.move(10, 100)

        self.n = QLabel('Задайте название событию', self)
        self.n.move(0, 120)
        self.n.setFont(QFont('Arial', 10))
        self.n.resize(500, 50)

        self.name_event = QLineEdit(self)
        self.name_event.move(0, 160)
        self.name_event.resize(220, 30)
        self.name_event.setText("")

        self.o = QLabel('Добавьте описание своего события', self)
        self.o.move(0, 200)
        self.o.setFont(QFont('Arial', 10))
        self.o.resize(500, 50)

        self.o1 = QLabel('(не обязательно)', self)
        self.o1.move(0, 220)
        self.o1.setFont(QFont('Arial', 10))
        self.o1.resize(500, 50)

        self.description = QLineEdit(self)
        self.description.move(0, 260)
        self.description.resize(300, 30)
        self.description.setText("Без описания")

        self.er = QLabel('Перед созданием убедитесь, что все поля заполнены!', self)
        self.er.move(0, 280)
        self.er.setFont(QFont('Arial', 10))
        self.er.resize(500, 50)

        self.creating_an_event = QPushButton(self)
        self.creating_an_event.move(10, 320)
        self.creating_an_event.resize(150, 30)
        self.creating_an_event.setText('Создать событие')
        self.creating_an_event.clicked.connect(self.create)
        self.creating_an_event.setStyleSheet('QPushButton {background-color: blue; color: white;}')

        self.pixmap = QPixmap('calendar.jpg')
        self.pixmap = self.pixmap.scaled(300, 300)
        self.image = QLabel(self)
        self.image.move(430, -10)
        self.image.resize(300, 300)
        self.image.setPixmap(self.pixmap)

        self.all_events = QPushButton(self)
        self.all_events.move(10, 370)
        self.all_events.resize(300, 30)
        self.all_events.setText('Посмотреть все события выбранного дня')
        self.all_events.setStyleSheet('QPushButton {background-color: blue; color: white;}')
        self.all_events.clicked.connect(self.all)

        self.calendar = QCalendarWidget(self)
        self.calendar.show()
        self.calendar.setGridVisible(True)
        self.calendar.move(340, 0)
        self.calendar.resize(400, 240)
        self.calendar.clicked.connect(self.dat)

        self.d = QLineEdit(self)
        self.date1 = self.calendar.selectedDate()
        self.d.setText(self.date1.toString())
        self.d.move(470, 270)
        self.d.resize(100, 30)
        self.d.setReadOnly(True)

        self.vd = QLabel('Выбор даты', self)
        self.vd.move(470, 230)
        self.vd.setFont(QFont('Arial', 10))
        self.vd.resize(500, 50)

    def dat(self):
        self.date1 = self.calendar.selectedDate().toString()
        self.d.setText(self.date1)

    def create(self):
        self.name = self.name_event.text()
        self.name1 = self.description.text()
        self.time1 = str(self.time.time().toPyTime())[:-3]
        if self.name == '' or self.name1 == '':
            self.w = Errorr()
            self.w.show()
        else:
            self.w = Creation()
            self.w.show()
            self.db2.cursor.execute('INSERT INTO Events (login, name, desc, date, time) VALUES (?, ?, ?, ?, ?)',
                                    (str(self.login), str(self.name), str(self.name1), str(self.date1),
                                    str(self.time1)))
            self.db2.save()
    def all(self):
        self.w = All_events(self.login, self)
        self.w.show()
        self.close()


class All_events(QMainWindow):
    def __init__(self, login, parent=None):
        super(All_events, self).__init__(parent)
        self.initUI()
        self.login = login

        self.table()

    def initUI(self):
        self.setGeometry(550, 100, 750, 710)
        self.setWindowTitle('Ваш Дневник Занятости')

    def table(self):
        self.login1 = self.login
        self.db = EventDB('Events.db')
        result = self.db.cursor.execute(f'SELECT * FROM Events').fetchall()
        result = [[v1, v2, v3, v4, v5] for v1, v2, v3, v4, v5 in result]
        res1 = {}
        for i in result:
            if i[0] in res1:
                res1[i[0]] += [i[1:]]
            else:
                res1[i[0]] = [i[1:]]
        if self.login not in res1:
            self.w = Err()
            self.w.show()
        else:
            k = 0
            listt = []
            for i in res1[self.login]:
                k += 1
                listt.append(i)
            self.res = QTableWidget(k, 4, self)
            self.res.move(10, 10)
            self.res.resize(800, 710)

            for i in range(k):
                item1 = QTableWidgetItem(listt[i][0])
                item1.setFlags(Qt.ItemIsEnabled)
                item1.setFont(QFont('Times New Roman', 12))
                self.res.setItem(i, 0, item1)

                item2 = QTableWidgetItem(str(listt[i][1]))
                item2.setFlags(Qt.ItemIsEnabled)
                item2.setFont(QFont('Times New Roman', 12))
                self.res.setItem(i, 1, item2)

                item3 = QTableWidgetItem(str(listt[i][2]))
                item3.setFlags(Qt.ItemIsEnabled)
                item3.setFont(QFont('Times New Roman', 12))
                self.res.setItem(i, 2, item3)

                item4 = QTableWidgetItem(str(listt[i][3]))
                item4.setFlags(Qt.ItemIsEnabled)
                item4.setFont(QFont('Times New Roman', 12))
                self.res.setItem(i, 3, item4)


class Err(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 350, 320, 100)
        self.setWindowTitle('!')

        self.o = QLabel('У вас нет текущих событий', self)
        self.o.move(30, 0)
        self.o.setFont(QFont('Arial', 10))
        self.o.resize(500, 50)

        self.ok = QPushButton(self)
        self.ok.move(80, 40)
        self.ok.resize(150, 30)
        self.ok.setText('ОК')
        self.ok.clicked.connect(self.okk)
        self.ok.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def okk(self):
        self.close()


class Creation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 350, 200, 100)
        self.setWindowTitle('')

        self.o = QLabel('Событие создано!', self)
        self.o.move(30, 0)
        self.o.setFont(QFont('Arial', 10))
        self.o.resize(500, 50)

        self.ok = QPushButton(self)
        self.ok.move(25, 40)
        self.ok.resize(150, 30)
        self.ok.setText('ОК')
        self.ok.clicked.connect(self.okk)
        self.ok.setStyleSheet('QPushButton {background-color: #A3C1DA}')

    def okk(self):
        self.close()


class Errorr(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 350, 320, 100)
        self.setWindowTitle('ОШИБКА')

        self.o = QLabel('Проверьте данные и повторите попытку', self)
        self.o.move(0, 0)
        self.o.setFont(QFont('Arial', 10))
        self.o.resize(500, 50)

        self.ok = QPushButton(self)
        self.ok.move(80, 40)
        self.ok.resize(150, 30)
        self.ok.setText('ОК')
        self.ok.clicked.connect(self.okk)
        self.ok.setStyleSheet('QPushButton {background-color: #A3C1DA}')

    def okk(self):
        self.close()


class Nl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 350, 320, 100)
        self.setWindowTitle('!')

        self.o = QLabel('Неверно введённый логин', self)
        self.o.move(30, 0)
        self.o.setFont(QFont('Arial', 10))
        self.o.resize(500, 50)

        self.ok = QPushButton(self)
        self.ok.move(80, 40)
        self.ok.resize(150, 30)
        self.ok.setText('ОК')
        self.ok.clicked.connect(self.okk)
        self.ok.setStyleSheet('QPushButton {background-color: #A3C1DA}')

    def okk(self):
        self.close()


class Np(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 350, 320, 100)
        self.setWindowTitle('!')

        self.o = QLabel('Неверно введённый пароль', self)
        self.o.move(30, 0)
        self.o.setFont(QFont('Arial', 10))
        self.o.resize(500, 50)

        self.ok = QPushButton(self)
        self.ok.move(80, 40)
        self.ok.resize(150, 30)
        self.ok.setText('ОК')
        self.ok.clicked.connect(self.okk)
        self.ok.setStyleSheet('QPushButton {background-color: #A3C1DA}')

    def okk(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = MainWindow()
    ma.show()
    sys.exit(app.exec())