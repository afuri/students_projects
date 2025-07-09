from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from Forms.message import Message


class DateChoosing(QWidget):
    submitted_date = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        uic.loadUi('ui/choosing_date.ui', self)
        self.setWindowIcon(QIcon('pictures/icon.png'))
        self.setWindowTitle(f'Stardew Valley Helper')

        self.OK_btn.clicked.connect(self.returning_chosen_date)

    def returning_chosen_date(self):
        if self.starting.text() not in [str(i) for i in range(1, 29)] or \
                self.finishing.text() not in [str(i) for i in range(1, 29)] or \
                int(self.finishing.text()) < int(self.starting.text()):
            self.err = Message('Неверный формат даты!')
            self.err.show()
        else:
            self.submitted_date.emit(f'{self.starting.text()} — {self.finishing.text()}')
            self.close()