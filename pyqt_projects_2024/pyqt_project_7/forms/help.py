from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont


class HelpForm(QWidget):
    def __init__(self, *nth):
        super().__init__()
        self.initUI(nth)

    def initUI(self, *nth):
        self.setWindowTitle('Справка')
        self.setGeometry(400, 400, 550, 500)

        file_rules = open('others/Немного правил.txt', 'r', encoding='utf-8')
        text_rules = file_rules.read()
        self.rules_lbl = QLabel(self)
        self.rules_lbl.setGeometry(10, 10, 500, 420)
        self.rules_lbl.setText(text_rules)
        font_rules = QFont('Calibri', 10)
        self.rules_lbl.setFont(font_rules)
        file_rules.close()

        self.underst_bt = QPushButton(self)
        font_underst = QFont('Calibri', 10)
        self.underst_bt.setGeometry(350, 430, 120, 40)
        self.underst_bt.setText('Понятно')
        self.underst_bt.setFont(font_underst)
        self.underst_bt.clicked.connect(self.close_wind)

    def close_wind(self):
        self.close()