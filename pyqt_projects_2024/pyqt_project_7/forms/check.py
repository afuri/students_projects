from PyQt5.QtWidgets import QPushButton, QLabel, QMessageBox, QWidget
from PyQt5.QtGui import QFont
from data import Data


class CheckForm(QWidget):
    def __init__(self, *sth, word='', answer=''):
        self.word = word
        self.ans = answer
        super().__init__()
        self.initUI(sth)

    def initUI(self, *sth):
        self.setWindowTitle('Проверка')
        self.setGeometry(1100, 500, 350, 200)

        self.title_ = QLabel(self)
        self.title_.move(90, 40)
        font_title = QFont('Calibri', 12)
        self.title_.setFont(font_title)
        if self.word == self.ans:
            Data.score += 1
            self.title_.setText('Молодец! Так держать!')

        elif self.word == '':
            self.know_ans = QPushButton(self)
            self.know_ans.setText('Ответ')
            self.know_ans.setGeometry(30, 120, 100, 50)
            font_ans = QFont('Calibri', 12)
            self.know_ans.setFont(font_ans)
            self.know_ans.clicked.connect(self.answer)
            self.title_.setText('Ты ничего не ответил:) \n Исправь это!')
        else:
            self.know_ans = QPushButton(self)
            self.know_ans.setText('Ответ')
            self.know_ans.setGeometry(30, 120, 100, 50)
            font_ans = QFont('Calibri', 12)
            self.know_ans.setFont(font_ans)
            self.know_ans.clicked.connect(self.answer)
            self.title_.setText('Неверно \n Попробуй ещё раз:)')

        self.thanks_bt = QPushButton(self)
        font_bt = QFont('Calibri', 12)
        self.thanks_bt.setFont(font_bt)
        self.thanks_bt.setGeometry(170, 120, 100, 50)
        self.thanks_bt.setText('Спасибо')
        self.thanks_bt.clicked.connect(self.close_check)

    def answer(self):
        self.right_ans = QMessageBox()
        self.right_ans.setWindowTitle('Ответ')
        self.right_ans.setText(self.ans)
        self.close_bt = self.right_ans.exec_()

    def close_check(self):
        self.close()