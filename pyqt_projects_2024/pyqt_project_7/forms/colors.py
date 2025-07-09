from random import choice
from PyQt5.QtGui import QFont, QPainter, QColor
from PyQt5.QtWidgets import QPushButton, QLabel, QMessageBox
from PyQt5.QtWidgets import QLineEdit, QWidget, QInputDialog
from data import Data
from forms.check import CheckForm
from DB.result_db import ResultDb


class ColorsForm(QWidget):
    def __init__(self, exitmenu):
        self.exitmenu = exitmenu
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 300, 800, 600)
        self.setWindowTitle('Цвета')

        self.text_input = QLineEdit(self)
        self.text_input.setGeometry(100, 350, 600, 30)
        font_text = QFont('Times New Roman', 12)
        self.text_input.setFont(font_text)

        self.next_task = QPushButton(self)
        font_task = QFont('Times New Roman', 12)
        self.next_task.setFont(font_task)
        self.next_task.setGeometry(280, 500, 200, 50)
        self.next_task.setText('Следующее задание')
        self.next_task.clicked.connect(self.next)

        self.finish_tasked = QPushButton(self)
        font_finish_task = QFont('Times New Roman', 12)
        self.finish_tasked.setFont(font_finish_task)
        self.finish_tasked.setGeometry(490, 500, 100, 50)
        self.finish_tasked.setText('Готово')
        self.finish_tasked.clicked.connect(self.check_task)

        self.exit_bt = QPushButton(self)
        font_exit = QFont('Times New Roman', 12)
        self.exit_bt.setFont(font_exit)
        self.exit_bt.setGeometry(600, 500, 100, 50)
        self.exit_bt.setText('Выйти')
        self.exit_bt.clicked.connect(self.exit)

        self.task_label = QLabel(self)
        self.task_label.setGeometry(290, 80, 400, 180)

        self.list_colors = ['red', 'black', 'white', 'yellow', 'orange', 'brown',
                            'grey', 'green', 'blue', 'purple', 'pink']
        self.ans = choice(self.list_colors)

        self.title = 'Цвета'

    def exit(self):
        if Data.score != 0:
            name_ok = QInputDialog.getText(self, "Имя", "Как тебя зовут?")
            Data.name = name_ok[0]
            if Data.name == '':
                self.no_name = QMessageBox()
                self.no_name.setWindowTitle('Нет имени')
                self.no_name.setText('Ты не написал свое имя!')
                self.no_name.setInformativeText('Исправь это!)')
                self.finish_bt = self.no_name.exec_()
            ResultDb(Data.name, self.title, Data.score)
        self.exitmenu.show()
        self.hide()

    def check_task(self):
        self.check_form = CheckForm(self, '', word=self.text_input.text(), answer=self.ans)
        self.check_form.show()

    def next(self):
        self.update()
        self.text_input.setText('')
        self.ans = choice(self.list_colors)

    def paintEvent(self, event):
        painter = QPainter(self)
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        painter.setPen(col)
        painter.setBrush(QColor(self.ans))
        painter.drawRect(300, 80, 180, 180)