from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtWidgets import QMainWindow
from data import Data
from forms.colors import ColorsForm
from forms.eng import EngForm
from forms.rus import RusForm
from forms.help import HelpForm
from forms.result import ResultForm
from forms.tems import TemsForm


class MenuForm(QMainWindow):
    def __init__(self):
        Data.flag = False
        Data.result = {}
        Data.score = 0
        Data.name = ''
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 200, 880, 595)
        self.setWindowTitle('PyQT_Progect')

        self.pixmap_tittle = QPixmap('others/Заголовок.png')
        self.title = QLabel(self)
        self.title.setGeometry(55, 35, 410, 50)
        self.title.setPixmap(self.pixmap_tittle)

        self.pixmap_image = QPixmap('others/Иконка.png')
        self.image = QLabel(self)
        self.image.setGeometry(710, 25, 200, 200)
        self.image.setPixmap(self.pixmap_image)

        file = open('others/Описание.txt', 'r', encoding='utf-8')
        text = file.read()
        self.describe = QLabel(self)
        self.describe.setGeometry(55, 72, 650, 400)
        self.describe.setText(text)
        font_describe = QFont('Calibri', 10)
        self.describe.setFont(font_describe)
        file.close()

        self.bt_settings = QPushButton(self)
        self.bt_settings.setText('Темы')
        font_settings = QFont('Times New Roman', 11)
        self.bt_settings.setFont(font_settings)
        self.bt_settings.setGeometry(55, 460, 150, 60)
        self.bt_settings.clicked.connect(self.tems_form_open)

        self.colors_bt = QPushButton(self)
        self.colors_bt.setText('Цвета')
        font_colors = QFont('Times New Roman', 11)
        self.colors_bt.setFont(font_colors)
        self.colors_bt.setGeometry(285, 460, 150, 60)
        self.colors_bt.clicked.connect(self.colors_form_open)

        self.rus_button = QPushButton(self)
        self.rus_button.setText('Рус → Англ')
        font_start = QFont('Times New Roman', 11)
        self.rus_button.setFont(font_start)
        self.rus_button.setGeometry(450, 460, 150, 60)
        self.rus_button.clicked.connect(self.rus_eng)

        self.eng_button = QPushButton(self)
        self.eng_button.setText('Англ → Рус')
        font_start = QFont('Times New Roman', 11)
        self.eng_button.setFont(font_start)
        self.eng_button.setGeometry(615, 460, 150, 60)
        self.eng_button.clicked.connect(self.eng_rus)

        self.bt_res = QPushButton(self)
        self.bt_res.setText('Результаты')
        font_bt_res = QFont('Times New Roman', 10)
        self.bt_res.setFont(font_bt_res)
        self.bt_res.setGeometry(715, 220, 120, 40)
        self.bt_res.clicked.connect(self.result_form_open)

        self.help_bt = QPushButton(self)
        font_help = QFont('Times New Roman', 10)
        self.help_bt.setFont(font_help)
        self.help_bt.setGeometry(715, 280, 120, 40)
        self.help_bt.setText('Справка')
        self.help_bt.clicked.connect(self.help)

    def tems_form_open(self):
        self.tems_form = TemsForm(self, '   Выбери тему(ы):')
        self.tems_form.show()

    def rus_eng(self):
        if Data.flag:
            self.rus_form = RusForm(self)
            self.rus_form.show()
            self.close()
        else:
            self.tems_form_open()

    def eng_rus(self):
        if Data.flag:
            self.eng_form = EngForm(self)
            self.eng_form.show()
            self.close()
        else:
            self.tems_form_open()

    def colors_form_open(self):
        self.colors_form = ColorsForm(self)
        self.colors_form.show()
        self.close()

    def help(self):
        self.help_form = HelpForm(self, '')
        self.help_form.show()

    def result_form_open(self):
        self.result_form = ResultForm(self, '')
        self.result_form.show()