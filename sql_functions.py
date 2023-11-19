import sqlite3
DATABASE_NAME: str = "coffee.sqlite"


def get_all_items() -> tuple:
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM coffee_item""").fetchall()
    con.close()
    return tuple(result)


def insert_row(sort, degree, is_ground, description, price, capacity):
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    cur.execute("""INSERT INTO coffee_item(sort, degree_of_roast, is_ground, flavour_description, price, capacity)
    VALUES (?, ?, ?, ?, ?, ?)""", (sort, degree, is_ground, description, price, capacity))
    con.commit()
