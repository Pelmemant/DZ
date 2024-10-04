import _sqlite3


def get_all_products():
    connection = _sqlite3.connect("initiate.db")
    cursor = connection.cursor()
    cursor.execute('SELECT  title, description, price FROM Products')
    records = cursor.fetchall()
    connection.close()
    return records
