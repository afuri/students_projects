from PyQt5 import QtCore, QtWidgets, uic, QtGui
import sqlite3
import sys


class Registration_Window(QtWidgets.QWidget):
    def __init__(self, res=''):
        super(Registration_Window, self).__init__()
        uic.loadUi('uic/register_wd.ui', self)
        self.res = res

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

        px = QtGui.QPixmap('images/fon1.jpg')
        px.scaled(100, 100)
        self.fon_lb.setPixmap(px)
        self.svor_bt.clicked.connect(lambda: self.showMinimized())
        self.pushButton.clicked.connect(self.save_to_database)

    def save_to_database(self):
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()
        result = self.res
        con = sqlite3.connect('users_db.sqlite')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, surname TEXT, result TEXT)')
        cur.execute('INSERT INTO users VALUES (?, ?, ?)', (name, surname, result))
        con.commit()
        con.close()

        self.pushButton.hide()
        self.lineEdit_name.hide()
        self.lineEdit_surname.hide()
        self.line.hide()
        self.line_2.hide()
        self.textBrowser.setText('Готово!\n\t   Ваш результат сохранён!')
        self.textBrowser.setStyleSheet('font: 20pt "MS Shell Dlg 2";')
        self.textBrowser.setAlignment(QtCore.Qt.AlignCenter)

        self.svor_bt.setIcon(QtGui.QIcon('images/close.png'))
        self.svor_bt.setIconSize(QtCore.QSize(20, 20))
        self.svor_bt.clicked.connect(lambda: sys.exit(app.exec_()))
        self.svor_bt.setStyleSheet('''QPushButton {
	background-color: rgb(193, 0, 0);
	color: rgb(255, 255, 255);
}
QPushButton:pressed{
	background-color: rgb(141, 0, 0);
	color: rgb(255, 255, 255);

}
        ''')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Registration_Window()
    sys.exit(app.exec_())
