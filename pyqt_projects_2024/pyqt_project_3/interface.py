import sys
import sqlite3
import random

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit
from PyQt5.QtWidgets import QButtonGroup, QRadioButton, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore

WORDS_NUMBER = 25
SENTENCES_NUMBER = 15

class NoValueError(Exception):
    pass


class NoUserInDatabaseError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


class AuthorisationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 100, 900, 800)
        self.setWindowTitle('Английский для детей')

        self.autorise = QLabel(self)
        self.autorise.resize(500, 100)
        self.autorise.move(130, 450)
        self.autorise.setFont(QFont('Times New Roman', 20))
        self.autorise.setText("Авторизация пользователя")

        self.login = QLabel(self)
        self.login.resize(100, 100)
        self.login.move(100, 525)
        self.login.setFont(QFont('Times New Roman', 15))
        self.login.setText("Логин:")

        self.password = QLabel(self)
        self.password.resize(100, 100)
        self.password.move(100, 600)
        self.password.setFont(QFont('Times New Roman', 15))
        self.password.setText("Пароль:")

        self.login_input = QLineEdit(self)
        self.login_input.resize(300, 35)
        self.login_input.move(225, 560)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.resize(300, 35)
        self.password_input.move(225, 635)

        self.data_enter = QPushButton('Ввести', self)
        self.data_enter.setFont(QFont('Times New Roman', 15))
        self.data_enter.resize(150, 50)
        self.data_enter.move(280, 690)
        self.data_enter.clicked.connect(self.open_main_menu)

        self.registrate = QPushButton('Регистрация', self)
        self.registrate.setFont(QFont('Times New Roman', 15))
        self.registrate.resize(200, 100)
        self.registrate.move(595, 570)
        self.registrate.clicked.connect(self.open_registration_window)

        self.pixmap1 = QPixmap('title_pic.png')
        self.title_pic = QLabel(self)
        self.title_pic.resize(275, 400)
        self.title_pic.move(615, 100)
        self.title_pic.setPixmap(self.pixmap1)

        self.pixmap2 = QPixmap('title_text.png')
        self.title_text = QLabel(self)
        self.title_text.resize(600, 400)
        self.title_text.move(5, 100)
        self.title_text.setPixmap(self.pixmap2)

        self.pixmap3 = QPixmap('title.png')
        self.title = QLabel(self)
        self.title.resize(600, 200)
        self.title.move(150, 0)
        self.title.setPixmap(self.pixmap3)

        self.authorisation_error = QMessageBox(self)

    def data_is_ok(self):
        entered_login = self.login_input.text()
        entered_password = self.password_input.text()
        if not entered_password or not entered_login:
            raise NoValueError
        connection = sqlite3.connect('users_database.db')
        cursor = connection.cursor()
        user_data = cursor.execute('SELECT * FROM Users_data WHERE login = ?',
                                   (entered_login,)).fetchone()
        connection.commit()
        connection.close()
        if not user_data:
            raise NoUserInDatabaseError
        if entered_password != user_data[1]:
            raise WrongPasswordError
        return True

    def open_main_menu(self):
        try:
            if self.data_is_ok():
                self.remember_user()
                self.login_input.clear()
                self.password_input.clear()
                self.main_menu = MainMenu()
                self.main_menu.show()
        except NoValueError:
            self.edit_error_message('Кажется, вы забыли ввести логин или пароль')
            self.authorisation_error.show()
        except NoUserInDatabaseError:
            self.edit_error_message('Такого пользователя не существует')
            self.authorisation_error.show()
        except WrongPasswordError:
            self.edit_error_message('Неверный пароль')
            self.authorisation_error.show()

    def open_registration_window(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()

    def edit_error_message(self, message):
        self.authorisation_error.setIcon(QMessageBox.Critical)
        self.authorisation_error.setText("Error")
        self.authorisation_error.setInformativeText(message)
        self.authorisation_error.setWindowTitle("Error")

    def remember_user(self):
        with open('users.txt', mode='w') as file:
            entered_login = self.login_input.text()
            file.write(entered_login)


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 100, 900, 800)
        self.setWindowTitle('Меню')

        self.choose_game = QLabel(self)
        self.choose_game.resize(500, 100)
        self.choose_game.move(325, 50)
        self.choose_game.setFont(QFont('Times New Roman', 30))
        self.choose_game.setText("Выбор игры")

        self.translate_words = QPushButton('Переведи слова', self)
        self.translate_words.setFont(QFont('Times New Roman', 15))
        self.translate_words.resize(275, 150)
        self.translate_words.move(325, 225)
        self.translate_words.clicked.connect(self.open_translations_game)

        self.complete_sentences = QPushButton('Дополни предложения', self)
        self.complete_sentences.setFont(QFont('Times New Roman', 15))
        self.complete_sentences.resize(275, 150)
        self.complete_sentences.move(325, 400)
        self.complete_sentences.clicked.connect(self.open_sentences_game)

        self.rating = QPushButton('Рейтинг пользователей', self)
        self.rating.setFont(QFont('Times New Roman', 15))
        self.rating.resize(275, 150)
        self.rating.move(325, 575)
        self.rating.clicked.connect(self.open_rating)

    def open_translations_game(self):
        self.translations_game = Translations()
        self.translations_game.show()

    def open_sentences_game(self):
        self.sentences_game = Sentences()
        self.sentences_game.show()

    def open_rating(self):
        self.rating_window = RatingWindow()
        self.rating_window.show()


class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 200, 600, 500)
        self.setWindowTitle('Регистрация')

        self.registration = QLabel(self)
        self.registration.resize(500, 100)
        self.registration.move(130, 100)
        self.registration.setFont(QFont('Times New Roman', 20))
        self.registration.setText("Регистрация пользователя")

        self.reg_login = QLabel(self)
        self.reg_login.resize(100, 100)
        self.reg_login.move(100, 175)
        self.reg_login.setFont(QFont('Times New Roman', 15))
        self.reg_login.setText("Логин:")

        self.reg_password = QLabel(self)
        self.reg_password.resize(100, 100)
        self.reg_password.move(100, 250)
        self.reg_password.setFont(QFont('Times New Roman', 15))
        self.reg_password.setText("Пароль:")

        self.reg_login_input = QLineEdit(self)
        self.reg_login_input.resize(300, 35)
        self.reg_login_input.move(225, 210)

        self.reg_password_input = QLineEdit(self)
        self.reg_password_input.resize(300, 35)
        self.reg_password_input.move(225, 285)

        self.new_data_enter = QPushButton('Ввести', self)
        self.new_data_enter.setFont(QFont('Times New Roman', 15))
        self.new_data_enter.resize(150, 50)
        self.new_data_enter.move(280, 340)
        self.new_data_enter.clicked.connect(self.registration_is_done)

        self.registration_error = QMessageBox(self)

    def registration_is_done(self):
        try:
            new_login = self.reg_login_input.text()
            new_password = self.reg_password_input.text()
            if not new_login or not new_password:
                raise NoValueError
            connection = sqlite3.connect('users_database.db')
            cursor = connection.cursor()
            checking = cursor.execute('SELECT * FROM Users_data WHERE login = ?',
                                      (new_login,)).fetchone()
            if checking:
                raise UserAlreadyExistsError
            cursor.execute('INSERT INTO Users_data (login, password) VALUES (?, ?)',
                           (new_login, new_password))
            connection.commit()
            connection.close()
            connection2 = sqlite3.connect('records_database.db')
            cursor2 = connection2.cursor()
            cursor2.execute('INSERT INTO Records (login, game1, game2) VALUES (?, ?, ?)',
                            (new_login, 0, 0))
            connection2.commit()
            connection2.close()
            self.close()
        except NoValueError:
            self.edit_error_message('Кажется, вы забыли ввести логин или пароль')
            self.registration_error.show()
        except UserAlreadyExistsError:
            self.edit_error_message('Пользователь с таким логином уже существует')
            self.registration_error.show()

    def edit_error_message(self, message):
        self.registration_error.setIcon(QMessageBox.Critical)
        self.registration_error.setText("Error")
        self.registration_error.setInformativeText(message)
        self.registration_error.setWindowTitle("Error")


class Translations(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 100, 900, 800)
        self.setWindowTitle('Переведи слова')

        self.instruction = QLabel(self)
        self.instruction.resize(500, 100)
        self.instruction.move(225, 100)
        self.instruction.setFont(QFont('Times New Roman', 20))
        self.instruction.setText("Введи перевод слова на английский")

        self.given_word = self.get_word_from_database()

        self.word = QLabel(self)
        self.word.resize(100, 100)
        self.word.move(425, 300)
        self.word.setFont(QFont('Times New Roman', 15))
        self.word.setText(self.given_word[1])

        self.enter_word = QLineEdit(self)
        self.enter_word.resize(300, 35)
        self.enter_word.move(300, 400)

        self.next_word = QPushButton('Ввести', self)
        self.next_word.setFont(QFont('Times New Roman', 15))
        self.next_word.resize(150, 50)
        self.next_word.move(280, 690)
        self.next_word.clicked.connect(self.show_next_word)

        self.end_word_game = QPushButton('Завершить', self)
        self.end_word_game.setFont(QFont('Times New Roman', 15))
        self.end_word_game.resize(150, 50)
        self.end_word_game.move(490, 690)
        self.end_word_game.clicked.connect(self.show_results_and_quit)

        self.question_number = 0
        self.correct_answers = 0

        self.results = QMessageBox(self)

    def show_next_word(self):
        self.question_number += 1
        if self.translation_is_correct():
            self.correct_answers += 1
        self.given_word = self.get_word_from_database()
        self.word.setText(self.given_word[1])
        self.enter_word.clear()

    def show_results_and_quit(self):
        self.results.setIcon(QMessageBox.Information)
        self.results.setText("Конец игры")
        self.results.setInformativeText(f'Ваш результат: {self.correct_answers} из {self.question_number}')
        self.results.setWindowTitle("Результаты")
        self.results.show()
        self.remember_record()
        self.close()

    def remember_record(self):
        with open('users.txt', mode='r') as file:
            current_user = file.readline()
        connection = sqlite3.connect('records_database.db')
        cursor = connection.cursor()
        if self.correct_answers > cursor.execute('SELECT * FROM Records WHERE login = ?',
                                                 (current_user,)).fetchone()[1]:
            cursor.execute('UPDATE Records SET game1 = ? WHERE login = ?',
                           (self.correct_answers, current_user))
        connection.commit()
        connection.close()

    def translation_is_correct(self):
        if self.given_word[2] == self.enter_word.text().lower():
            return True
        return False

    def get_word_from_database(self):
        connection = sqlite3.connect('words_database.db')
        cursor = connection.cursor()
        word = cursor.execute('SELECT * FROM Words WHERE id = ?',
                              (str(random.randrange(1, WORDS_NUMBER + 1)),)).fetchone()
        connection.commit()
        connection.close()
        return word


class Sentences(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 100, 900, 800)
        self.setWindowTitle('Дополни предложения')

        self.instruction = QLabel(self)
        self.instruction.resize(650, 100)
        self.instruction.move(175, 100)
        self.instruction.setFont(QFont('Times New Roman', 20))
        self.instruction.setText("Выбери, как нужно дополнить предложение")

        self.given_sentence, self.answers = self.get_sentence_from_database()

        self.sentence = QLabel(self)
        self.sentence.resize(700, 100)
        self.sentence.move(150, 250)
        self.sentence.setFont(QFont('Times New Roman', 15))
        self.sentence.setText(self.given_sentence[1])

        self.answer1 = QRadioButton(self)
        self.answer1.resize(200, 20)
        self.answer1.move(300, 350)
        self.answer1.setText(self.answers[1])
        self.answer1.setFont(QFont('Times New Roman', 12))
        self.answer1.nextCheckState()

        self.answer2 = QRadioButton(self)
        self.answer2.resize(200, 20)
        self.answer2.move(300, 400)
        self.answer2.setText(self.answers[2])
        self.answer2.setFont(QFont('Times New Roman', 12))

        self.answer3 = QRadioButton(self)
        self.answer3.resize(200, 20)
        self.answer3.move(300, 450)
        self.answer3.setText(self.answers[3])
        self.answer3.setFont(QFont('Times New Roman', 12))

        self.answer4 = QRadioButton(self)
        self.answer4.resize(200, 20)
        self.answer4.move(300, 500)
        self.answer4.setText(self.answers[4])
        self.answer4.setFont(QFont('Times New Roman', 12))

        self.sentence_answers = QButtonGroup(self)
        self.sentence_answers.addButton(self.answer1)
        self.sentence_answers.addButton(self.answer2)
        self.sentence_answers.addButton(self.answer3)
        self.sentence_answers.addButton(self.answer4)

        self.next_sentence = QPushButton('Подтвердить', self)
        self.next_sentence.setFont(QFont('Times New Roman', 15))
        self.next_sentence.resize(150, 50)
        self.next_sentence.move(280, 690)
        self.next_sentence.clicked.connect(self.show_next_sentence)

        self.end_sentence_game = QPushButton('Завершить', self)
        self.end_sentence_game.setFont(QFont('Times New Roman', 15))
        self.end_sentence_game.resize(150, 50)
        self.end_sentence_game.move(490, 690)
        self.end_sentence_game.clicked.connect(self.show_results_and_quit)

        self.question_number = 0
        self.correct_answers = 0

        self.results = QMessageBox(self)

    def show_next_sentence(self):
        self.question_number += 1
        if self.answer_is_correct():
            self.correct_answers += 1
        self.given_sentence, self.answers = self.get_sentence_from_database()
        self.sentence.setText(self.given_sentence[1])
        self.answer1.setText(self.answers[1])
        self.answer2.setText(self.answers[2])
        self.answer3.setText(self.answers[3])
        self.answer4.setText(self.answers[4])

    def show_results_and_quit(self):
        self.results.setIcon(QMessageBox.Information)
        self.results.setText("Конец игры")
        self.results.setInformativeText(f'Ваш результат: {self.correct_answers} из {self.question_number}')
        self.results.setWindowTitle("Результаты")
        self.results.show()
        self.remember_record()
        self.close()

    def remember_record(self):
        with open('users.txt', mode='r') as file:
            current_user = file.readline()
        connection = sqlite3.connect('records_database.db')
        cursor = connection.cursor()
        if self.correct_answers > cursor.execute('SELECT * FROM Records WHERE login = ?',
                                                 (current_user,)).fetchone()[2]:
            cursor.execute('UPDATE Records SET game2 = ? WHERE login = ?',
                           (self.correct_answers, current_user))
        connection.commit()
        connection.close()

    def answer_is_correct(self):
        if self.answers[self.given_sentence[2]] == self.sentence_answers.checkedButton().text():
            return True
        return False

    def get_sentence_from_database(self):
        connection = sqlite3.connect('sentences_database.db')
        cursor = connection.cursor()
        sentence = cursor.execute('SELECT * FROM Sentences WHERE id = ?',
                                  (str(random.randrange(1, SENTENCES_NUMBER + 1)),)).fetchone()
        answer = cursor.execute('SELECT * FROM Answers WHERE id = ?',
                                (sentence[0],)).fetchone()
        connection.commit()
        connection.close()
        return sentence, answer


class RatingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 100, 900, 800)
        self.setWindowTitle('Рейтинг пользователей')

        self.rating_head = QLabel(self)
        self.rating_head.resize(650, 100)
        self.rating_head.move(250, 10)
        self.rating_head.setFont(QFont('Times New Roman', 25))
        self.rating_head.setText("Рейтинг пользователей")

        self.rating1 = QLabel(self)
        self.rating1.resize(350, 100)
        self.rating1.move(100, 100)
        self.rating1.setFont(QFont('Times New Roman', 15))
        self.rating1.setText("Лучшие переводчики")

        self.rating2 = QLabel(self)
        self.rating2.resize(350, 100)
        self.rating2.move(550, 100)
        self.rating2.setFont(QFont('Times New Roman', 15))
        self.rating2.setText("Лучшие граммотеи")

        self.results_of_game1 = QTableWidget(5, 2, self)
        self.results_of_game1.setHorizontalHeaderItem(0, QTableWidgetItem('Пользователь'))
        self.results_of_game1.setHorizontalHeaderItem(1, QTableWidgetItem('Результат'))
        self.results_of_game1.move(0, 200)
        self.results_of_game1.resize(450, 550)

        self.results_of_game2 = QTableWidget(5, 2, self)
        self.results_of_game2.setHorizontalHeaderItem(0, QTableWidgetItem('Пользователь'))
        self.results_of_game2.setHorizontalHeaderItem(1, QTableWidgetItem('Результат'))
        self.results_of_game2.move(450, 200)
        self.results_of_game2.resize(450, 550)

        for i in range(5):
            self.results_of_game1.setRowHeight(i, 100)
            self.results_of_game2.setRowHeight(i, 100)
        for i in range(2):
            self.results_of_game1.setColumnWidth(i, 200)
            self.results_of_game2.setColumnWidth(i, 200)

        connection = sqlite3.connect('records_database.db')
        cursor = connection.cursor()
        data1 = cursor.execute('SELECT * FROM Records ORDER BY game1 DESC').fetchall()
        data2 = cursor.execute('SELECT * FROM Records ORDER BY game2 DESC').fetchall()
        connection.commit()
        connection.close()

        for i in range(5):
            item1 = QTableWidgetItem(data1[i][0])
            item1.setFlags(QtCore.Qt.ItemIsEnabled)
            item1.setFont(QFont('Times New Roman', 12))
            self.results_of_game1.setItem(i, 0, item1)

            item2 = QTableWidgetItem(str(data1[i][1]))
            item2.setFlags(QtCore.Qt.ItemIsEnabled)
            item2.setFont(QFont('Times New Roman', 12))
            self.results_of_game1.setItem(i, 1, item2)

            item3 = QTableWidgetItem(data2[i][0])
            item3.setFlags(QtCore.Qt.ItemIsEnabled)
            item3.setFont(QFont('Times New Roman', 12))
            self.results_of_game2.setItem(i, 0, item3)

            item4 = QTableWidgetItem(str(data2[i][2]))
            item4.setFlags(QtCore.Qt.ItemIsEnabled)
            item4.setFont(QFont('Times New Roman', 12))
            self.results_of_game2.setItem(i, 1, item4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AuthorisationWindow()
    win.show()
    sys.exit(app.exec())