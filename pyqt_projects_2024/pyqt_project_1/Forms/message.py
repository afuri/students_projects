from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog


class Message(QDialog):
    def __init__(self, text):
        super().__init__()
        uic.loadUi('ui/error.ui', self)
        self.setWindowTitle('Внимание!')
        self.setWindowIcon(QIcon('pictures/icon.png'))
        self.setWhatsThis("Будьте аккуратны")

        self.label.setText(text)
        self.OK.clicked.connect(self.closing)

    def closing(self):
        self.close()