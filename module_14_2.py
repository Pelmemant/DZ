import _sqlite3

connection = _sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute("SELECT COUNT(*) FROM users")
total_count = cursor.fetchone()[0]


cursor.execute("SELECT SUM(balance) FROM users")
sum_balances = cursor.fetchone()[0]


average_balance = sum_balances / total_count
print(f"Средний баланс: {average_balance}")


connection.commit()
connection.close()