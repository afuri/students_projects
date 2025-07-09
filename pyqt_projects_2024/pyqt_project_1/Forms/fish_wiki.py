import csv
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget
from Forms.message import Message


class FishWiki(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/fish.ui', self)
        self.setWindowIcon(QIcon('pictures/fish/Anchovy.png'))
        self.setWindowTitle(f'Stardew Valley Helper: Fish')
        self.labels = ['self.label_difficulty',
                       'self.label_type',
                       'self.label_time',
                       'self.label_weather',
                       'self.label_description',
                       'self.label_name',
                       'self.label_place',
                       'self.label_season']
        self.button_group.buttonClicked.connect(self.showing_fish)
        self.question_button.clicked.connect(self.help)

    def help(self):
        self.message = Message("""Чтобы увидеть информацию о рыбе, нажмите на кнопку рядом с ней.""")
        self.message.show()

    def showing_fish(self, btn):
        with open('DB/FISH_DB.csv', encoding='windows-1251') as fish_file:
            fish_table = csv.DictReader(fish_file, delimiter=';')
            fish_table = list(fish_table)

        for fish in fish_table:
            if fish['name'] == btn.text():
                fish_info = fish
                break

        for lbl in self.labels:
            eval(lbl).setText(fish_info[lbl[11:]])
            if fish['Легенда, 1/0'] == '1':
                self.legend = Message("""Это легендарная рыба! 
Для ловли не забудьте прокачать навык рыбной ловли и взять наживку и снасти.""")
                self.legend.show()

        self.label_pic.setPixmap(QPixmap(f'pictures/fish/{fish_info['pic']}'))