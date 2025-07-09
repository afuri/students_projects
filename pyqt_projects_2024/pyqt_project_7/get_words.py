import sqlite3


def get_words(list_choice):
    con = sqlite3.connect('Tasks.db')
    cur = con.cursor()
    list_choice = tuple(list_choice)
    if len(list_choice) == 1:
        ids = cur.execute(f"SELECT id FROM themes WHERE topic = ?", list_choice).fetchall()
        ids = tuple([i[0] for i in ids])
        words = cur.execute(f"SELECT * FROM tasks WHERE theme = ?", ids).fetchall()
        words = {i[1]: i[2] for i in words}
    else:
        ids = cur.execute(f"SELECT id FROM themes WHERE topic IN {list_choice}").fetchall()
        ids = tuple([i[0] for i in ids])
        words = cur.execute(f"SELECT * FROM tasks WHERE theme IN {ids}").fetchall()
        words = {i[1]: i[2] for i in words}
    con.close()
    return words


