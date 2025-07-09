from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog


class Opening(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/opening_window.ui', self)
        self.setWindowTitle('Что я умею?')
        self.setWindowIcon(QIcon('pictures/icon.png'))
        self.setWhatsThis(":)")

        self.OK.clicked.connect(self.closing)

    def closing(self):
        self.close()