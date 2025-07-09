from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from Forms.calendar import Calendar


class SeasonChoosing(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/choosing_season.ui', self)
        self.setWindowIcon(QIcon('pictures/icon.png'))
        self.setWindowTitle('Stardew Valley Helper')

        self.spring_button.clicked.connect(lambda: self.run_calendar('spring'))
        self.summer_button.clicked.connect(lambda: self.run_calendar('summer'))
        self.fall_button.clicked.connect(lambda: self.run_calendar('fall'))

    def run_calendar(self, season):
        files_of_seasons = {'spring': 'ui/spring.ui', 'summer': 'ui/summer.ui', 'fall': 'ui/fall.ui'}
        self.seasonal_calendar = Calendar(files_of_seasons[season], season)
        self.seasonal_calendar.show()
        self.close()