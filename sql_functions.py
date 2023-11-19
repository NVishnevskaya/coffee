import sqlite3
DATABASE_NAME: str = "coffee.sqlite"


def get_all_items() -> tuple:
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM coffee_item""").fetchall()
    con.close()
    return tuple(result)
