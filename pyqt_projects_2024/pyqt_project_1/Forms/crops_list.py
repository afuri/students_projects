from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget


class ListOfCrops(QWidget):
    submitted_crop = QtCore.pyqtSignal(str)

    def __init__(self, season):
        self.season = season
        super().__init__()
        uic.loadUi(f'ui/{season}_crops.ui', self)
        self.setWindowIcon(QIcon(f'pictures/crops/{season}/{season}_icon.png'))
        self.setWindowTitle(season)

        self.crops_group.buttonToggled.connect(self.returning_chosen_crop)

    def returning_chosen_crop(self, crop):
        self.submitted_crop.emit(crop.text())
        self.close()