import sqlite3
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from Forms.picking_date import DateChoosing
from Forms.crops_list import ListOfCrops
from Forms.message import Message


class Calendar(QWidget):
    def __init__(self, name_of_calendar, season):
        super().__init__()
        uic.loadUi(name_of_calendar, self)
        self.setWindowIcon(QIcon(f'pictures/crops/{season}/{season}_icon.png'))
        self.setWindowTitle(f'Stardew Valley Helper: {season.title()}')

        self.season = season

        self.crop_is_chosen = False
        self.chosen_crop = 0

        self.date_is_chosen = False
        self.chosen_date = ''

        self.question_button.clicked.connect(self.help)
        self.choosing_crop_button.clicked.connect(self.choosing_crop)
        self.choosing_date_button.clicked.connect(self.choosing_date)
        self.calc_button.clicked.connect(self.calculating)

    def help(self):
        self.message = Message("""Чтобы рассчитать, в какие дни будет урожай, и сколько он вам принесёт, выберите 
растение и дату.""")
        self.message.show()
    def choosing_date(self):
        self.date = DateChoosing()
        self.date.submitted_date.connect(self.update_date)
        self.date.show()

    def choosing_crop(self):
        self.list_of_crops = ListOfCrops(self.season)
        self.list_of_crops.submitted_crop.connect(self.update_crop)
        self.list_of_crops.show()

    @QtCore.pyqtSlot(str)
    def update_date(self, date):
        self.chosen_date = date
        self.label_for_date.setText(self.chosen_date)
        self.date_is_chosen = True

    @QtCore.pyqtSlot(str)
    def update_crop(self, name_of_crop):
        self.chosen_crop = name_of_crop
        self.label_for_crop.setText(self.chosen_crop)
        self.crop_is_chosen = True

    def calculating(self):
        if self.chosen_crop == 0:
            self.err = Message('Не выбрано растение!')
            self.err.show()

        elif self.chosen_date == '':
            self.err = Message('Не выбраны дни!')
            self.err.show()
        else:
            bg_colors = {'spring': [(170, 255, 127), (0, 213, 0)],
                         'summer': [(255, 184, 250), (255, 107, 228)],
                         'fall': [(255, 232, 51), (255, 189, 56)]}

            for i in range(1, 29):
                btn = eval(f'self.pushButton_{i}')
                btn.setStyleSheet(f"""background-color: rgb{bg_colors[self.season][0]};
                border-style: outset;
                border-color: rgb{bg_colors[self.season][1]};
                border-width: 3px""")
            starting, finishing = self.chosen_date.split(' — ')
            plant_name = self.chosen_crop

            con = sqlite3.connect('DB/crops_DB')
            cur = con.cursor()

            plant_info = cur.execute(f"""SELECT id, price, days_to_grow 
                                         FROM Crops
                                         WHERE Crops.name = '{plant_name}' """).fetchall()[0]

            plant_id, plant_price, plant_duration = plant_info

            cur.execute(f"""INSERT INTO History(crop_id, start, finish) 
                            VALUES({plant_id}, {starting}, {finishing})""")

            con.commit()

            counter = 0
            for i in range(int(starting) + int(plant_duration), int(finishing) + 1, int(plant_duration) + 1):
                counter += 1
                btn = eval(f'self.pushButton_{i}')
                btn.setStyleSheet(f"""background-color: rgb{bg_colors[self.season][1]}; 
                border-style: outset;
                border-color: rgb{bg_colors[self.season][1]}; 
                border-width: 3px""")
            else:
                if int(finishing) == 28:
                    eval('self.pushButton_28').setStyleSheet('background-color : red')
                    self.err = Message('Внимание! После 28 дня растение сгниёт.')
                    self.err.show()
                self.label_price.setText(str(plant_price * counter))

            if counter == 0:
                self.err = Message('У вас ничего не успеет вырасти :(')
                self.err.show()
                for i in range(1, 29):
                    btn = eval(f'self.pushButton_{i}')
                    btn.setStyleSheet(f"""background-color: rgb{bg_colors[self.season][0]};
                    border-style: outset;
                    border-color: rgb{bg_colors[self.season][1]};
                    border-width: 3px""")

