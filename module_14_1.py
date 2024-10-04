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

for i in range(10):
    cursor.execute(
        'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
        (f'newusers{i+1}',f'example{i+1}@gmail.com', f'{i*10+10}', '1000'))

a = 1
while a < 10:
    cursor.execute('UPDATE Users SET balance = ? where id = ?', (500, f'{a}'))
    a += 2

b = 1
while b < 10:
    cursor.execute('DELETE FROM Users WHERE id = ?', (f'{b}'))
    b += 3

cursor.execute('SELECT  username, email, age, balance FROM Users WHERE age != 60')
records = cursor.fetchall()

for record in records:
    username, email, age, balance = record
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

connection.commit()
connection.close()