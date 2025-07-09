import sys
from PyQt5.QtWidgets import QApplication
from forms.menu import MenuForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MenuForm()
    ex.show()
    sys.exit(app.exec())
