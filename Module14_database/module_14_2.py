import sqlite3


connection = sqlite3.connect('not_telegram2.db')
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
# age = 10
# for i in range(10):
#     connection.execute(f"INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
#                        (f'User{i+1}', f'example{i+1}@gmail.com', age, f'10000'))
#     age += 10
#
# cursor.execute("SELECT username, age, balance FROM Users")
# users = cursor.fetchall()
# for user in users[::2]:
#     cursor.execute(f"UPDATE Users SET balance = ? WHERE username = ?", ("500", user[0]))
#
# for user in users[::3]:
#     cursor.execute("DELETE FROM Users WHERE username = ?", [user[0]],)
#
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", ('60',))
# users = cursor.fetchall()
# for user in users:
#     print(user)

#cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchone()[0]
print(all_balance/total_users)

#connection.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

connection.commit()
connection.close()