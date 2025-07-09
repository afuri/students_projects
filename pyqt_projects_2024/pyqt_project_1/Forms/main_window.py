from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from Forms.fish_wiki import FishWiki
from Forms.choosing_season import SeasonChoosing
from Forms.opening import Opening


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main_window.ui', self)
        self.setWindowIcon(QIcon('pictures/icon.png'))
        self.setWindowTitle('Stardew Valley Helper')

        self.fishing_button.clicked.connect(self.opening_fish)
        self.calendar_button.clicked.connect(self.opening_calendar)
        self.what_button.clicked.connect(self.help)

    def opening_fish(self):
        self.fish = FishWiki()
        self.fish.show()

    def opening_calendar(self):
        self.choosing_season = SeasonChoosing()
        self.choosing_season.show()

    def help(self):
        self.message = Opening()
        self.message.show()

