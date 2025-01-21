import sqlite3


connection = sqlite3.connect('not_telegram.db')
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
age = 10
for i in range(10):
    connection.execute(f"INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
                       (f'User{i+1}', f'example{i+1}@gmail.com', age, f'10000'))
    age += 10

cursor.execute("SELECT username, age, balance FROM Users")
users = cursor.fetchall()
for user in users[::2]:
    cursor.execute(f"UPDATE Users SET balance = ? WHERE username = ?", ("500", user[0]))

for user in users[::3]:
    cursor.execute("DELETE FROM Users WHERE username = ?", [user[0]],)

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", ('60',))
users = cursor.fetchall()
for user in users:
    print(user)

#connection.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

connection.commit()
connection.close()