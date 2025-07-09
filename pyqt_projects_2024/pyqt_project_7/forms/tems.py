from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QMessageBox
from PyQt5.QtWidgets import QWidget, QCheckBox
from get_words import get_words
from data import Data


class TemsForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Настройки')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()

        self.box_nums = QCheckBox('Числа', self)
        self.box_nums.setGeometry(70, 40, 100, 50)

        self.box_family = QCheckBox('Люди', self)
        self.box_family.setGeometry(70, 100, 100, 50)

        self.box_house = QCheckBox('Дом', self)
        self.box_house.setGeometry(70, 160, 50, 50)

        self.box_parts = QCheckBox('Части тела', self)
        self.box_parts.setGeometry(70, 220, 150, 50)

        self.box_animals = QCheckBox('Животные', self)
        self.box_animals.setGeometry(70, 280, 150, 50)

        self.box_wear = QCheckBox('Одежда', self)
        self.box_wear.setGeometry(70, 340, 100, 50)

        self.box_food = QCheckBox('Еда', self)
        self.box_food.setGeometry(70, 400, 50, 50)

        self.box_school = QCheckBox('Школа', self)
        self.box_school.setGeometry(200, 40, 100, 50)

        self.box_nature = QCheckBox('Природа', self)
        self.box_nature.setGeometry(200, 100, 100, 50)

        self.finish_bt = QPushButton('Готово', self)
        font_finish = QFont('Calibri', 12)
        self.finish_bt.setFont(font_finish)
        self.finish_bt.setGeometry(300, 400, 100, 50)
        self.finish_bt.clicked.connect(self.save_choice_task)

        self.list_boxes = [self.box_nums, self.box_family, self.box_house,
                           self.box_parts, self.box_animals, self.box_wear,
                           self.box_food, self.box_school, self.box_nature]

    def themes(self):
        self.list_choice = []
        for i in self.list_boxes:
            if i.isChecked():
                self.list_choice.append(i.text())

    def save_choice_task(self):
        self.themes()
        if len(self.list_choice) != 0:
            Data.flag = True
            print('Выбрано:', '\n'.join(self.list_choice))
            Data.result = get_words(self.list_choice)
            self.close()
        else:
            self.no_tems = QMessageBox()
            self.no_tems.setWindowTitle('Нет темы')
            self.no_tems.setText('Ты не выбрал ни одной темы!')
            self.no_tems.setInformativeText('Исправь это!)')
            self.finish_bt = self.no_tems.exec_()