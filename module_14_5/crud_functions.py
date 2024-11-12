import _sqlite3

connection = _sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
connection.commit()


def add_user(username, email, age):
    cursor.execute(
        'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
        (f'{username}', f'{email}', f'{age}', '1000'))
    connection.commit()




def is_included(name):
    cursor.execute('SELECT username FROM Users')
    all_name = cursor.fetchall()
    print(all_name)
    try_name = (f'{name}',)
    connection.commit()
    if try_name in all_name:
        return True
    else:
        return False



def get_all_products():
    cursor.execute('SELECT  title, description, price FROM Products')
    records = cursor.fetchall()
    connection.commit()
    return records


def off_shout():
    connection.close()
