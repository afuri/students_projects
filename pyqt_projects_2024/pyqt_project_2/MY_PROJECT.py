import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QMessageBox

import sqlite3


class LoginDatabase():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def is_table(self, table_name):
        query = "SELECT name from sqlite_master WHERE type='table' AND name='{}';".format(table_name)
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True


class Start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Найди схожий")
        self.setGeometry(500, 80, 900, 900)

        self.start = QPixmap("other_pic/start.jpg")
        self.image = QLabel(self)
        self.image.move(40, 10)
        self.image.resize(886, 320)
        self.image.setPixmap(self.start)

        self.registration = QPushButton('Регистрация', self)
        self.registration.move(165, 700)
        self.registration.resize(150, 60)
        self.registration.setFont(QFont('Times', 12))

        self.enter = QPushButton('Войти', self)
        self.enter.move(600, 700)
        self.enter.resize(150, 60)
        self.enter.setFont(QFont('Times', 12))

        self.ui_components()  # функция для текста крутящегося
        self.show()

        self.loginDatabase = LoginDatabase('login.db')
        if self.loginDatabase.is_table('USERS'):
            pass
        else:
            self.loginDatabase.conn.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,PASSWORD TEXT)")
            self.loginDatabase.conn.execute("INSERT INTO USERS VALUES(?, ?)",
                                            ('admin', 'admin'))
            self.loginDatabase.conn.commit()
        self.enter.clicked.connect(self.enter_open_window)
        self.registration.clicked.connect(self.registration_open_window)

    def enter_open_window(self):
        self.close()

        self.enter_example_window = Enter()
        self.enter_example_window.show()

    def registration_open_window(self):
        self.registration_open_window = Registration()
        self.registration_open_window.show()

    def ui_components(self):
        with open('start_text.txt', 'r', encoding='utf-8') as file:
            text = str(file.read())

        label = ScrollLabel(self)
        label.setText(text)
        label.setFont(QFont('Times', 14))
        label.setGeometry(150, 400, 600, 240)


class ScrollLabel(QScrollArea):

    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)
        content = QWidget(self)
        self.setWidget(content)
        lay = QVBoxLayout(content)
        self.label = QLabel(content)

        self.label.setWordWrap(True)
        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)

    def text(self):
        get_text = self.label.text()
        return get_text


class Enter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Вход")
        self.setGeometry(600, 450, 700, 300)

        self.text_login = QLabel(self)
        self.text_login.setText("Логин:")
        self.text_login.move(170, 20)
        self.text_login.setFont(QFont('Times', 12))

        self.login = QLineEdit(self)
        self.login.setFont(QFont('Times', 14))
        self.login.move(170, 60)
        self.login.resize(300, 50)

        self.text_password = QLabel(self)
        self.text_password.setText("Пароль:")
        self.text_password.move(170, 120)
        self.text_password.setFont(QFont('Times', 12))

        self.password = QLineEdit(self)
        self.password.setFont(QFont('Times', 14))
        self.password.move(170, 150)
        self.password.resize(300, 50)
        self.password.setEchoMode(QLineEdit.Password)

        self.input = QPushButton('Войти', self)
        self.input.move(170, 210)
        self.input.resize(150, 50)
        self.input.setFont(QFont('Times', 12))
        self.input.clicked.connect(self.loginCheck)

        self.loginDatabase = LoginDatabase('login.db')

    def loginCheck(self):
        username = self.login.text()
        password = self.password.text()
        if (not username) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return msg

        result = self.loginDatabase.conn.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",
                                                 (username, password))
        if len(result.fetchall()):
            self.close()  # закрываем "своё" окно класса

            self.open_main_window = Main()
            self.open_main_window.show()

            self.loginDatabase.conn.close()
        else:
            msg = QMessageBox.information(self, 'Внимание!', 'Неправильное имя пользователя или пароль.')
            return msg


class Registration(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Регистрация")
        self.setGeometry(600, 450, 600, 450)

        self.text_name = QLabel(self)
        self.text_name.setText("Имя:")
        self.text_name.move(250, 20)
        self.text_name.setFont(QFont("Times", 12))

        self.name = QLineEdit(self)
        self.name.setFont(QFont('Times', 14))
        self.name.move(130, 50)
        self.name.resize(300, 40)

        self.text_new_login = QLabel(self)
        self.text_new_login.setText("Логин:")
        self.text_new_login.move(250, 95)
        self.text_new_login.setFont(QFont("Times", 12))

        self.new_login = QLineEdit(self)
        self.new_login.setFont(QFont('Times', 14))
        self.new_login.move(130, 130)
        self.new_login.resize(300, 40)

        self.text_new_password = QLabel(self)
        self.text_new_password.setText("Пароль:")
        self.text_new_password.move(250, 175)
        self.text_new_password.setFont(QFont("Times", 12))

        self.new_password1 = QLineEdit(self)
        self.new_password1.setFont(QFont('Times', 14))
        self.new_password1.move(130, 210)
        self.new_password1.resize(300, 40)
        self.new_password1.setEchoMode(QLineEdit.Password)

        self.text_new_password = QLabel(self)
        self.text_new_password.setText("Повторите Пароль:")
        self.text_new_password.move(200, 260)
        self.text_new_password.setFont(QFont("Times", 12))

        self.new_password2 = QLineEdit(self)
        self.new_password2.setFont(QFont('Times', 14))
        self.new_password2.move(130, 300)
        self.new_password2.resize(300, 40)
        self.new_password2.setEchoMode(QLineEdit.Password)

        self.add_new_user = QPushButton('Зарегистрироваться', self)
        self.add_new_user.move(130, 370)
        self.add_new_user.resize(300, 50)
        self.add_new_user.setFont(QFont('Times', 14))
        self.add_new_user.clicked.connect(self.insertData)

        self.loginDatabase = LoginDatabase('login.db')

    def insertData(self):
        username = self.new_login.text()
        password1 = self.new_password1.text()
        password2 = self.new_password2.text()

        if (not username) or (not password1):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return msg

        elif password2 != password1:
            msg = QMessageBox.information(self, 'Внимание!', 'Пароли не одинаковы')
            return msg

        result = self.loginDatabase.conn.execute("SELECT * FROM USERS WHERE USERNAME = ?", (username,))

        if result.fetchall():
            msg = QMessageBox.information(self, 'Внимание!', 'Пользоватеть с таким именем уже зарегистрирован.')
            return msg

        else:
            self.loginDatabase.conn.execute("INSERT INTO USERS VALUES(?, ?)",
                                            (username, password1))
            self.loginDatabase.conn.commit()
            self.close()


class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Основное меню")
        self.setGeometry(500, 80, 900, 900)

        self.example = QPushButton('Обучение', self)
        self.example.move(30, 20)
        self.example.resize(150, 60)
        self.example.setFont(QFont('Times', 16))
        self.example.clicked.connect(self.example_open_window)

        self.choice_difficult_text = QLabel(self)
        self.choice_difficult_text.setText("Выберите игру")
        self.choice_difficult_text.move(310, 100)
        self.choice_difficult_text.setFont(QFont('Times', 16))

        self.figure = QPixmap("figure/figure2.jpg")
        self.image = QLabel(self)
        self.image.move(430, 170)
        self.image.resize(330, 270)
        self.image.setPixmap(self.figure)

        self.figure_play_st = QPushButton('ФИГУРЫ', self)
        self.figure_play_st.move(140, 240)
        self.figure_play_st.resize(190, 50)
        self.figure_play_st.setFont(QFont('Times', 16))
        self.figure_play_st.clicked.connect(self.figure_play_open_window)

        self.figure = QPixmap("symbol/symbol_picture.jpg")
        self.image = QLabel(self)
        self.image.move(430, 480)
        self.image.resize(330, 300)
        self.image.setPixmap(self.figure)

        self.symbol_play_st = QPushButton('CИМВОЛЫ', self)
        self.symbol_play_st.move(140, 560)
        self.symbol_play_st.resize(190, 50)
        self.symbol_play_st.setFont(QFont('Times', 16))
        self.symbol_play_st.clicked.connect(self.symbol_play_open_window)

        self.example = QPushButton('Правила', self)
        self.example.move(710, 20)
        self.example.resize(150, 60)
        self.example.setFont(QFont('Times', 16))
        self.example.clicked.connect(self.rules_game)

    def rules_game(self):
        self.open_window_rules = Rules()
        self.open_window_rules.show()

    def figure_play_open_window(self):
        self.close()

        self.figure_play_open = Figure()
        self.figure_play_open.show()

    def symbol_play_open_window(self):
        self.close()

        self.symbol_play_open = Symbol()
        self.symbol_play_open.show()

    def example_open_window(self):
        self.example_open_window = Example()
        self.example_open_window.show()

        self.close()


class Rules(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Найди схожий")
        self.setGeometry(500, 80, 600, 600)

        with open('rules.txt', 'r', encoding='utf-8') as file:
            text = str(file.read())

        label = ScrollLabel(self)
        label.setText(text)
        label.setFont(QFont('Times', 14))
        label.setGeometry(10, 20, 580, 500)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Обучение")
        self.setGeometry(500, 80, 900, 900)

        self.input = QPushButton("LET'S GOOOO!!!!", self)
        self.input.move(300, 350)
        self.input.resize(320, 150)
        self.input.setFont(QFont('Times', 24))
        self.input.clicked.connect(self.open_picture)

        self.text_task = QLabel(self)
        self.text_task.setText("Дорогой пользователь, сейчас тебе представляется возможность\n"
                               "пройти обучение. По правилам данной игры,\n"
                               "Вы сейчас сможете увидеть картинку, которую, надо запомнить\n"
                               "и соотнести с одной из представленных картинок в следующем окне.\n"
                               "Удачи!")
        self.text_task.move(100, 100)
        self.text_task.setFont(QFont('Times', 14))

    def open_picture(self):
        self.close()

        self.example_picture = Picture()
        self.example_picture.show()


class Picture(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Картинка")
        self.setGeometry(690, 280, 450, 450)

        self.start = QPixmap("example/example_pic.jpg")
        self.image = QLabel(self)
        self.image.move(15, 15)
        self.image.resize(400, 400)
        self.image.setPixmap(self.start)

        self.open_example_task = Task()
        QTimer.singleShot(2999, self.open_example_task.show)  # ждем несколько секунд и открываем окно с заданиями
        QTimer.singleShot(3000, self.close)  # ждем нескольео секунд и закрываем окно


class Task(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Задание")
        self.setGeometry(500, 80, 900, 900)

        self.text_task = QLabel(self)
        self.text_task.setText("Выберите верную картинку:")
        self.text_task.move(300, 20)
        self.text_task.setFont(QFont('Times', 14))

        self.example_false1 = QPixmap("example/example_false1.jpg")
        self.image = QLabel(self)
        self.image.move(20, 80)
        self.image.setPixmap(self.example_false1)

        self.example_false2 = QPixmap("example/example_false2.jpg")
        self.image = QLabel(self)
        self.image.move(440, 80)
        self.image.setPixmap(self.example_false2)

        self.example_false3 = QPixmap("example/example_false3.jpg")
        self.image = QLabel(self)
        self.image.move(20, 490)
        self.image.setPixmap(self.example_false3)

        self.example_pic = QPixmap("example/example_pic.jpg")
        self.image = QLabel(self)
        self.image.move(440, 490)
        self.image.setPixmap(self.example_pic)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        if 490 <= self.y <= 890 and 440 <= self.x <= 840:
            self.close()

            self.answertrue_example_window = AnswerTrue()
            self.answertrue_example_window.show()

        else:
            self.close()

            self.answerfalse_example_window = AnswerFalse()
            self.answerfalse_example_window.show()


class AnswerTrue(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно Победителя")
        self.setGeometry(690, 280, 450, 450)

        self.text_win = QLabel(self)
        self.text_win.setText("Это верная картинка.\nВернемся в основное меню?")
        self.text_win.move(70, 100)
        self.text_win.setFont(QFont('Times', 14))

        self.bt_yes = QPushButton("Да!)", self)
        self.bt_yes.move(150, 250)
        self.bt_yes.resize(100, 50)
        self.bt_yes.setFont(QFont('Times', 14))
        self.bt_yes.clicked.connect(self.return_main_window)

    def return_main_window(self):
        self.close()

        self.open_main_window = Main()
        self.open_main_window.show()


class AnswerFalse(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно Проиграша")
        self.setGeometry(690, 280, 450, 450)

        self.text_loose = QLabel(self)
        self.text_loose.setText("Ой!Картинка не верна.\nХотите попробывать еще раз?")
        self.text_loose.move(70, 100)
        self.text_loose.setFont(QFont('Times', 14))

        self.bt_yes = QPushButton("Да!)", self)
        self.bt_yes.move(60, 250)
        self.bt_yes.resize(100, 50)
        self.bt_yes.setFont(QFont('Times', 14))
        self.bt_yes.clicked.connect(self.open_picture)

        self.bt_no = QPushButton("Нет(", self)
        self.bt_no.move(290, 250)
        self.bt_no.resize(100, 50)
        self.bt_no.setFont(QFont('Times', 14))
        self.bt_no.clicked.connect(self.return_main_window)

    def open_picture(self):
        self.close()

        self.example_picture = Picture()
        self.example_picture.show()

    def return_main_window(self):
        self.close()

        self.open_main_window = Main()
        self.open_main_window.show()


class Figure(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Фигуры")
        self.setGeometry(500, 80, 900, 900)

        self.first_lvl_bt = QPushButton('1 уровень', self)
        self.first_lvl_bt.move(40, 40)
        self.first_lvl_bt.resize(190, 50)
        self.first_lvl_bt.setFont(QFont('Times', 16))
        self.first_lvl_bt.clicked.connect(self.first_lvl_figure)
        self.first_lvl_bt.setStyleSheet('QPushButton {background-color: #1E90FF; color: white}')

        self.second_lvl_bt = QPushButton('2 уровень', self)
        self.second_lvl_bt.move(40, 340)
        self.second_lvl_bt.resize(190, 50)
        self.second_lvl_bt.setFont(QFont('Times', 16))
        self.second_lvl_bt.clicked.connect(self.second_lvl_figure)
        self.second_lvl_bt.setStyleSheet('QPushButton {background-color: #1E90FF; color: white}')

        self.third_lvl_bt = QPushButton('3 уровень', self)
        self.third_lvl_bt.move(40, 640)
        self.third_lvl_bt.resize(190, 50)
        self.third_lvl_bt.setFont(QFont('Times', 16))
        self.third_lvl_bt.clicked.connect(self.third_lvl_figure)
        self.third_lvl_bt.setStyleSheet('QPushButton {background-color: #1E90FF; color: white}')

        self.choice = QPixmap("other_pic/choice_figure.png")
        self.image = QLabel(self)
        self.image.move(340, 160)
        self.image.resize(510, 510)
        self.image.setPixmap(self.choice)

        self.return_main_bt = QPushButton('Основное меню', self)
        self.return_main_bt.move(500, 800)
        self.return_main_bt.resize(220, 50)
        self.return_main_bt.setFont(QFont('Times', 16))
        self.return_main_bt.clicked.connect(self.return_main_window)
        self.return_main_bt.setStyleSheet('QPushButton {background-color: #1E90FF; color: white}')

    def first_lvl_figure(self):
        self.close()

        self.open_figure1lvl_window = Figure_1lvl_Picture()
        self.open_figure1lvl_window.show()

    def second_lvl_figure(self):
        self.close()

        self.open_figure2lvl_window = Figure_2lvl_Picture()
        self.open_figure2lvl_window.show()

    def third_lvl_figure(self):
        self.close()

        self.open_figure3lvl_window = Figure_3lvl_Picture()
        self.open_figure3lvl_window.show()

    def return_main_window(self):
        self.close()

        self.open_main_window = Main()
        self.open_main_window.show()


class Figure_1lvl_Picture(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Картинка")
        self.setGeometry(690, 280, 450, 450)

        self.start = QPixmap("figure/figure_lvl1.png")
        self.image = QLabel(self)
        self.image.move(15, 15)
        self.image.resize(400, 400)
        self.image.setPixmap(self.start)

        self.open_figure1lvl_window = Figure_1lvl()
        QTimer.singleShot(1999, self.open_figure1lvl_window.show)  # ждем несколько секунд и открываем окно с заданиями
        QTimer.singleShot(2000, self.close)  # ждем нескольео секунд и закрываем окно


class Figure_1lvl(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Задание")
        self.setGeometry(500, 80, 900, 900)

        self.text_task = QLabel(self)
        self.text_task.setText("Выберите верную картинку:")
        self.text_task.move(300, 20)
        self.text_task.setFont(QFont('Times', 14))

        self.lvl1 = QPixmap("figure/figure_lvl1.png")
        self.image = QLabel(self)
        self.image.move(20, 80)
        self.image.setPixmap(self.lvl1)

        self.lvl1_f2 = QPixmap("figure/figure_lvl1_f2.png")
        self.image = QLabel(self)
        self.image.move(440, 80)
        self.image.setPixmap(self.lvl1_f2)

        self.lvl1_f3 = QPixmap("figure/figure_lvl1_f3.png")
        self.image = QLabel(self)
        self.image.move(20, 490)
        self.image.setPixmap(self.lvl1_f3)

        self.lvl1_f1 = QPixmap("figure/figure_lvl1_f1.png")
        self.image = QLabel(self)
        self.image.move(440, 490)
        self.image.setPixmap(self.lvl1_f1)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        if 80 <= self.y <= 480 and 20 <= self.x <= 420:
            self.close()

            self.answertrue_window = AnswerTrue()
            self.answertrue_window.show()

        else:
            self.close()

            self.answerfalse_figure_window = AnswerFalseFigureLvl1()
            self.answerfalse_figure_window.show()


class AnswerFalseFigureLvl1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно Проиграша")
        self.setGeometry(690, 280, 450, 450)

        self.text_loose = QLabel(self)
        self.text_loose.setText("Ой!Картинка не верна.\nХотите попробывать еще раз?")
        self.text_loose.move(70, 100)
        self.text_loose.setFont(QFont('Times', 14))

        self.bt_yes = QPushButton("Да!)", self)
        self.bt_yes.move(60, 250)
        self.bt_yes.resize(100, 50)
        self.bt_yes.setFont(QFont('Times', 14))
        self.bt_yes.clicked.connect(self.open_lvl1)

        self.bt_no = QPushButton("Нет(", self)
        self.bt_no.move(290, 250)
        self.bt_no.resize(100, 50)
        self.bt_no.setFont(QFont('Times', 14))
        self.bt_no.clicked.connect(self.return_main_window)

    def open_lvl1(self):
        self.close()

        self.Figurelvl1_picture = Figure_1lvl_Picture()
        self.Figurelvl1_picture.show()

    def return_main_window(self):
        self.close()

        self.open_main_window = Main()
        self.open_main_window.show()


class Figure_2lvl_Picture(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Картинка")
        self.setGeometry(690, 280, 450, 450)

        self.start = QPixmap("figure/figure_lvl2.jpg")
        self.image = QLabel(self)
        self.image.move(15, 15)
        self.image.resize(400, 400)
        self.image.setPixmap(self.start)

        self.open_figure2lvl_window = Figure_2lvl()
        QTimer.singleShot(1999, self.open_figure2lvl_window.show)  # ждем несколько секунд и открываем окно с заданиями
        QTimer.singleShot(2000, self.close)  # ждем нескольео секунд и закрываем окно


class Figure_2lvl(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Задание")
        self.setGeometry(500, 80, 900, 900)

        self.text_task = QLabel(self)
        self.text_task.setText("Выберите верную картинку:")
        self.text_task.move(300, 20)
        self.text_task.setFont(QFont('Times', 14))

        self.lvl2 = QPixmap("figure/figure_lvl2.jpg")
        self.image = QLabel(self)
        self.image.move(20, 80)
        self.image.setPixmap(self.lvl2)

        self.lvl2_f1 = QPixmap("figure/figure_lvl2_f1.jpg")
        self.image = QLabel(self)
        self.image.move(440, 80)
        self.image.setPixmap(self.lvl2_f1)

        self.lvl2_f2 = QPixmap("figure/figure_lvl2_f2.jpg")
        self.image = QLabel(self)
        self.image.move(20, 490)
        self.image.setPixmap(self.lvl2_f2)

        self.lvl2_f3 = QPixmap("figure/figure_lvl2_f3.jpg")
        self.image = QLabel(self)
        self.image.move(440, 490)
        self.image.setPixmap(self.lvl2_f3)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        if 80 <= self.y <= 480 and 20 <= self.x <= 420:
            self.close()

            self.answertrue_window = AnswerTrue()
            self.answertrue_window.show()

        else:
            self.close()

            self.answerfalse_figure_window = AnswerFalseFigureLvl2()
            self.answerfalse_figure_window.show()


class AnswerFalseFigureLvl2(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно Проиграша")
        self.setGeometry(690, 280, 450, 450)

        self.text_loose = QLabel(self)
        self.text_loose.setText("Ой!Картинка не верна.\nХотите попробывать еще раз?")
        self.text_loose.move(70, 100)
        self.text_loose.setFont(QFont('Times', 14))

        self.bt_yes = QPushButton("Да!)", self)
        self.bt_yes.move(60, 250)
        self.bt_yes.resize(100, 50)
        self.bt_yes.setFont(QFont('Times', 14))
        self.bt_yes.clicked.connect(self.open_lvl2)

        self.bt_no = QPushButton("Нет(", self)
        self.bt_no.move(290, 250)
        self.bt_no.resize(100, 50)
        self.bt_no.setFont(QFont('Times', 14))
        self.bt_no.clicked.connect(self.return_main_window)

    def open_lvl2(self):
        self.close()

        self.Figurelvl2_picture = Figure_2lvl_Picture()
        self.Figurelvl2_picture.show()

    def return_main_window(self):
        self.close()

        self.open_main_window = Main()
        self.open_main_window.show()


class Figure_3lvl_Picture(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Картинка")
        self.setGeometry(690, 280, 450, 450)

        self.start = QPixmap("figure/figure_lvl3.jpg")
        self.image = QLabel(self)
        self.image.move(15, 15)
        self.image.resize(400, 400)
        self.image.setPixmap(self.start)

        self.open_figure3lvl_window = Figure_3lvl()
        QTimer.singleShot(1999, self.open_figure3lvl_window.show)  # ждем несколько секунд и открываем окно с заданиями
        QTimer.singleShot(2000, self.close)  # ждем нескольео секунд и закрываем окно


class Figure_3lvl(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Задание")
        self.setGeometry(500, 80, 900, 900)

        self.text_task = QLabel(self)
        self.text_task.setText("Выберите верную картинку:")
        self.text_task.move(300, 20)
        self.text_task.setFont(QFont('Times', 14))

        self.lvl3_f1 = QPixmap("figure/figure_lvl3_f1.jpg")
        self.image = QLabel(self)
        self.image.move(20, 80)
        self.image.setPixmap(self.lvl3_f1)

        self.lvl3 = QPixmap("figure/figure_lvl3.jpg")
        self.image = QLabel(self)
        self.image.move(440, 80)
        self.image.setPixmap(self.lvl3)

        self.lvl3_f2 = QPixmap("figure/figure_lvl3_f2.jpg")
        self.image = QLabel(self)
        self.image.move(20, 490)
        self.image.setPixmap(self.lvl3_f2)

        self.lvl3_f3 = QPixmap("figure/figure_lvl3_f3.jpg")
        self.image = QLabel(self)
        self.image.move(440, 490)
        self.image.setPixmap(self.lvl3_f3)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        if 80 <= self.y <= 480 and 440 <= self.x <= 840:
            self.close()

            self.answertrue_window = AnswerTrue()
            self.answertrue_window.show()

        else:
            self.close()

            self.answerfalse_figure_window = AnswerFalseFigureLvl3()
            self.answerfalse_figure_window.show()


class AnswerFalseFigureLvl3(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно Проиграша")
        self.setGeometry(690, 280, 450, 450)

        self.text_loose = QLabel(self)
        self.text_loose.setText("Ой!Картинка не верна.\nХотите попробывать еще раз?")
        self.text_loose.move(70, 100)
        self.text_loose.setFont(QFont('Times', 14))

        self.bt_yes = QPushButton("Да!)", self)
        self.bt_yes.move(60, 250)
        self.bt_yes.resize(100, 50)
        self.bt_yes.setFont(QFont('Times', 14))
        self.bt_yes.clicked.connect(self.open_lvl3)

        self.bt_no = QPushButton("Нет(", self)
        self.bt_no.move(290, 250)
        self.bt_no.resize(100, 50)
        self.bt_no.setFont(QFont('Times', 14))
        self.bt_no.clicked.connect(self.return_main_window)

    def open_lvl3(self):
        self.close()

        self.Figurelvl3_picture = Figure_3lvl_Picture()
        self.Figurelvl3_picture.show()

    def return_main_window(self):
        self.close()

        self.open_main_window = Main()
        self.open_main_window.show()


class Symbol(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Символы")
        self.setGeometry(500, 80, 900, 900)

        self.first_lvl_bt = QPushButton('1 уровень', self)
        self.first_lvl_bt.move(40, 40)
        self.first_lvl_bt.resize(190, 50)
        self.first_lvl_bt.setFont(QFont('Times', 16))
        self.first_lvl_bt.clicked.connect(self.first_lvl_symbol)
        self.first_lvl_bt.setStyleSheet('QPushButton {background-color: #FF0000	; color: white}')

        self.second_lvl_bt = QPushButton('2 уровень', self)
        self.second_lvl_bt.move(40, 340)
        self.second_lvl_bt.resize(190, 50)
        self.second_lvl_bt.setFont(QFont('Times', 16))
        self.second_lvl_bt.clicked.connect(self.second_lvl_symbol)
        self.second_lvl_bt.setStyleSheet('QPushButton {background-color: #FF0000 ; color: white}')

        self.third_lvl_bt = QPushButton('3 уровень', self)
        self.third_lvl_bt.move(40, 640)
        self.third_lvl_bt.resize(190, 50)
        self.third_lvl_bt.setFont(QFont('Times', 16))
        self.third_lvl_bt.clicked.connect(self.third_lvl_symbol)
        self.third_lvl_bt.setStyleSheet('QPushButton {background-color: #FF0000	; color: white}')

        self.choice = QPixmap("other_pic/choice_symbol.png")
        self.image = QLabel(self)
        self.image.move(340, 160)
        self.image.resize(510, 510)
        self.image.setPixmap(self.choice)

        self.return_main_bt = QPushButton('Основное меню', self)
        self.return_main_bt.move(500, 800)
        self.return_main_bt.resize(220, 50)
        self.return_main_bt.setFont(QFont('Times', 16))
        self.return_main_bt.clicked.connect(self.return_main_window)
        self.return_main_bt.setStyleSheet('QPushButton {background-color: #FF0000	; color: white}')

    def first_lvl_symbol(self):
        self.close()

        self.open_symbol1lvl_window = Symbol_1lvl_Picture()
        self.open_symbol1lvl_window.show()

    def second_lvl_symbol(self):
        self.close()

        self.open_symbol2lvl_window = Symbol_2lvl_Picture()
        self.open_symbol2lvl_window.show()

    def third_lvl_symbol(self):
        self.close()

        self.open_symbol3lvl_window = Symbol_3lvl_Picture()
        self.open_symbol3lvl_window.show()

    def return_main_window(self):
        self.close()

        self.open_main_window = Main()
        self.open_main_window.show()


class Symbol_1lvl_Picture(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Картинка")
        self.setGeometry(690, 280, 450, 450)

        self.start = QPixmap("symbol/symbol_lvl1.jpg")
        self.image = QLabel(self)
        self.image.move(15, 15)
        self.image.resize(400, 400)
        self.image.setPixmap(self.start)

        self.open_symbol1lvl_window = Symbol_1lvl()
        QTimer.singleShot(1999, self.open_symbol1lvl_window.show)  # ждем несколько секунд и открываем окно с заданиями
        QTimer.singleShot(2000, self.close)  # ждем нескольео секунд и закрываем окно


class Symbol_1lvl(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Задание")
        self.setGeometry(500, 80, 900, 900)

        self.text_task = QLabel(self)
        self.text_task.setText("Выберите верную картинку:")
        self.text_task.move(300, 20)
        self.text_task.setFont(QFont('Times', 14))

        self.lvl1 = QPixmap("symbol/symbol_lvl1.jpg")
        self.image = QLabel(self)
        self.image.move(20, 80)
        self.image.setPixmap(self.lvl1)

        self.lvl1_f2 = QPixmap("symbol/symbol_lvl1_f2.jpg")
        self.image = QLabel(self)
        self.image.move(440, 80)
        self.image.setPixmap(self.lvl1_f2)

        self.lvl1_f3 = QPixmap("symbol/symbol_lvl1_f3.jpg")
        self.image = QLabel(self)
        self.image.move(20, 490)
        self.image.setPixmap(self.lvl1_f3)

        self.lvl1_f1 = QPixmap("symbol/symbol_lvl1_f1.jpg")
        self.image = QLabel(self)
        self.image.move(440, 490)
        self.image.setPixmap(self.lvl1_f1)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        if 80 <= self.y <= 480 and 20 <= self.x <= 420:
            self.close()

            self.answertrue_window = AnswerTrue()
            self.answertrue_window.show()

        else:
            self.close()

            self.answerfalse_symbol_window = AnswerFalseSymbolLvl1()
            self.answerfalse_symbol_window.show()


class AnswerFalseSymbolLvl1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно Проиграша")
        self.setGeometry(690, 280, 450, 450)

        self.text_loose = QLabel(self)
        self.text_loose.setText("Ой!Картинка не верна.\nХотите попробывать еще раз?")
        self.text_loose.move(70, 100)
        self.text_loose.setFont(QFont('Times', 14))

        self.bt_yes = QPushButton("Да!)", self)
        self.bt_yes.move(60, 250)
        self.bt_yes.resize(100, 50)
        self.bt_yes.setFont(QFont('Times', 14))
        self.bt_yes.clicked.connect(self.open_lvl1_symbol)

        self.bt_no = QPushButton("Нет(", self)
        self.bt_no.move(290, 250)
        self.bt_no.resize(100, 50)
        self.bt_no.setFont(QFont('Times', 14))
        self.bt_no.clicked.connect(self.return_main_window)

    def open_lvl1_symbol(self):
        self.close()

        self.symbol_lvl1_picture = Symbol_1lvl_Picture()
        self.symbol_lvl1_picture.show()

    def return_main_window(self):
        self.close()

        self.open_main_window = Main()
        self.open_main_window.show()


class Symbol_2lvl_Picture(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Картинка")
        self.setGeometry(690, 280, 450, 450)

        self.start = QPixmap("symbol/symbol_lvl2.jpg")
        self.image = QLabel(self)
        self.image.move(15, 15)
        self.image.resize(400, 400)
        self.image.setPixmap(self.start)

        self.open_symbol2lvl_window = Symbol_2lvl()
        QTimer.singleShot(1999, self.open_symbol2lvl_window.show)  # ждем несколько секунд и открываем окно с заданиями
        QTimer.singleShot(2000, self.close)  # ждем нескольео секунд и закрываем окно


class Symbol_2lvl(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Задание")
        self.setGeometry(500, 80, 900, 900)

        self.text_task = QLabel(self)
        self.text_task.setText("Выберите верную картинку:")
        self.text_task.move(300, 20)
        self.text_task.setFont(QFont('Times', 14))

        self.lvl2 = QPixmap("symbol/symbol_lvl2.jpg")
        self.image = QLabel(self)
        self.image.move(20, 80)
        self.image.setPixmap(self.lvl2)

        self.lvl2_f1 = QPixmap("symbol/symbol_lvl2_f1.jpg")
        self.image = QLabel(self)
        self.image.move(440, 80)
        self.image.setPixmap(self.lvl2_f1)

        self.lvl2_f2 = QPixmap("symbol/symbol_lvl2_f2.jpg")
        self.image = QLabel(self)
        self.image.move(20, 490)
        self.image.setPixmap(self.lvl2_f2)

        self.lvl2_f3 = QPixmap("symbol/symbol_lvl2_f3.jpg")
        self.image = QLabel(self)
        self.image.move(440, 490)
        self.image.setPixmap(self.lvl2_f3)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        if 80 <= self.y <= 480 and 20 <= self.x <= 420:
            self.close()

            self.answertrue_window = AnswerTrue()
            self.answertrue_window.show()

        else:
            self.close()

            self.answerfalse_figure_window = AnswerFalseSymbolLvl2()
            self.answerfalse_figure_window.show()


class AnswerFalseSymbolLvl2(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно Проиграша")
        self.setGeometry(690, 280, 450, 450)

        self.text_loose = QLabel(self)
        self.text_loose.setText("Ой!Картинка не верна.\nХотите попробывать еще раз?")
        self.text_loose.move(70, 100)
        self.text_loose.setFont(QFont('Times', 14))

        self.bt_yes = QPushButton("Да!)", self)
        self.bt_yes.move(60, 250)
        self.bt_yes.resize(100, 50)
        self.bt_yes.setFont(QFont('Times', 14))
        self.bt_yes.clicked.connect(self.open_lvl2)

        self.bt_no = QPushButton("Нет(", self)
        self.bt_no.move(290, 250)
        self.bt_no.resize(100, 50)
        self.bt_no.setFont(QFont('Times', 14))
        self.bt_no.clicked.connect(self.return_main_window)

    def open_lvl2(self):
        self.close()

        self.symbol_lvl2_picture = Symbol_2lvl_Picture()
        self.symbol_lvl2_picture.show()

    def return_main_window(self):
        self.close()

        self.open_main_window = Main()
        self.open_main_window.show()


class Symbol_3lvl_Picture(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Картинка")
        self.setGeometry(690, 280, 450, 450)

        self.start = QPixmap("symbol/symbol_lvl3.jpg")
        self.image = QLabel(self)
        self.image.move(15, 15)
        self.image.resize(400, 400)
        self.image.setPixmap(self.start)

        self.open_symbol3lvl_window = Symbol_3lvl()
        QTimer.singleShot(1999, self.open_symbol3lvl_window.show)  # ждем несколько секунд и открываем окно с заданиями
        QTimer.singleShot(2000, self.close)  # ждем нескольео секунд и закрываем окно


class Symbol_3lvl(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Задание")
        self.setGeometry(500, 80, 900, 900)

        self.text_task = QLabel(self)
        self.text_task.setText("Выберите верную картинку:")
        self.text_task.move(300, 20)
        self.text_task.setFont(QFont('Times', 14))

        self.lvl2 = QPixmap("symbol/symbol_lvl3.jpg")
        self.image = QLabel(self)
        self.image.move(20, 80)
        self.image.setPixmap(self.lvl2)

        self.lvl2_f1 = QPixmap("symbol/symbol_lvl3_f1.jpg")
        self.image = QLabel(self)
        self.image.move(440, 80)
        self.image.setPixmap(self.lvl2_f1)

        self.lvl2_f2 = QPixmap("symbol/symbol_lvl3_f2.jpg")
        self.image = QLabel(self)
        self.image.move(20, 490)
        self.image.setPixmap(self.lvl2_f2)

        self.lvl2_f3 = QPixmap("symbol/symbol_lvl3_f3.jpg")
        self.image = QLabel(self)
        self.image.move(440, 490)
        self.image.setPixmap(self.lvl2_f3)

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        if 80 <= self.y <= 480 and 20 <= self.x <= 420:
            self.close()

            self.answertrue_window = AnswerTrue()
            self.answertrue_window.show()

        else:
            self.close()

            self.answerfalse_figure_window = AnswerFalseSymbolLvl3()
            self.answerfalse_figure_window.show()


class AnswerFalseSymbolLvl3(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно Проиграша")
        self.setGeometry(690, 280, 450, 450)

        self.text_loose = QLabel(self)
        self.text_loose.setText("Ой!Картинка не верна.\nХотите попробывать еще раз?")
        self.text_loose.move(70, 100)
        self.text_loose.setFont(QFont('Times', 14))

        self.bt_yes = QPushButton("Да!)", self)
        self.bt_yes.move(60, 250)
        self.bt_yes.resize(100, 50)
        self.bt_yes.setFont(QFont('Times', 14))
        self.bt_yes.clicked.connect(self.open_lvl2)

        self.bt_no = QPushButton("Нет(", self)
        self.bt_no.move(290, 250)
        self.bt_no.resize(100, 50)
        self.bt_no.setFont(QFont('Times', 14))
        self.bt_no.clicked.connect(self.return_main_window)

    def open_lvl2(self):
        self.close()

        self.symbol_lvl3_picture = Symbol_3lvl_Picture()
        self.symbol_lvl3_picture.show()

    def return_main_window(self):
        self.close()

        self.open_main_window = Main()
        self.open_main_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    st = Start()
    st.show()
    sys.exit(app.exec())
