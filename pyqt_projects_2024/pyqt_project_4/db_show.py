from PyQt5 import QtCore, QtWidgets, uic, QtGui
import sqlite3
import sys


class Database_Show(QtWidgets.QWidget):
    def __init__(self):
        super(Database_Show, self).__init__()
        uic.loadUi('uic/database_show.ui', self)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

        self.fon_lb.setPixmap(QtGui.QPixmap('images/fon1.jpg'))
        # self.back_bt.clicked.connect(lambda: self.showMinimized())
        self.pushButton.clicked.connect(self.show_database)

    def show_database(self):
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()
        con = sqlite3.connect('users_db.sqlite')
        cur = con.cursor()

        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 90)
        self.table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('Имя'))
        self.table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('Фамилия'))
        self.table.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Результат'))

        cur.execute(f"SELECT name, surname, result FROM users WHERE name='{name}' AND surname='{surname}'")
        result = cur.fetchone()
        if result:
            self.table.setRowCount(1)
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem(f'{result[0]}'))
            self.table.setItem(0, 1, QtWidgets.QTableWidgetItem(f'{result[1]}'))
            self.table.setItem(0, 2, QtWidgets.QTableWidgetItem(f'{result[2]}'))
        else:
            self.table.setColumnCount(1)
            self.table.setRowCount(1)
            self.table.setColumnWidth(0, 350)
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem('Ничего не найдено'))

        con.close()

    def closeEvent(self, event):
        event.ignore()

