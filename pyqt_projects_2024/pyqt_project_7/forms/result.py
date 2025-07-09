import sqlite3

from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem


class ResultForm(QWidget):
    def __init__(self, *mth):
        super().__init__()
        self.initUI(mth)

    def initUI(self, *mth):
        self.setWindowTitle('Результаты')
        self.setGeometry(1100, 300, 500, 400)
        self.get_results()

    def get_results(self):
        results = sqlite3.connect('Results.db')
        cur = results.cursor()
        results = cur.execute('SELECT * FROM Res').fetchall()
        self.table = QTableWidget(self)
        self.table.setRowCount(len(results))
        self.table.setColumnCount(4)
        self.table.setColumnWidth(0, 90)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 90)
        self.table.setColumnWidth(3, 160)
        QTableWidget.resizeRowsToContents(self.table)
        self.table.setHorizontalHeaderLabels(["Имя", "Задание", "Результат", "Дата"])
        for i, row in enumerate(results):
            row = row[1:]
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)
        self.table.move(0, 0)
        self.table.resize(500, 400)