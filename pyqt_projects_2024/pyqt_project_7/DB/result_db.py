import sqlite3
from datetime import datetime


class ResultDb:
    def __init__(self, name, title, score):
        self.name = name
        self.title = title
        self.score = score
        result_db = sqlite3.connect('Results.db')
        cur = result_db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Res (
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             task TEXT NOT NULL,
                             score TEXT NOT NULL,
                             datetime TEXT)''')

        date_time = str(datetime.today().strftime('%d-%m-%Y, %H:%M'))

        cur.execute('INSERT INTO Res (name, task, score, datetime) VALUES (?, ?, ?, ?)',
                    (self.name, self.title, self.score, date_time))
        result_db.commit()
        cur.close()

