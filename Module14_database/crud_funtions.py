import sqlite3




def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

def insert_products(product_title, description, price):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Products (title, description, price) VALUES(?, ?, ?)",
                   (f"{product_title}", f"{description}", f"{price}")
                   )
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    title = cursor.fetchall()
    connection.commit()
    connection.close()
    return title




def add_user(username, email, age):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    if not is_included(username):
        cursor.execute(f"INSERT INTO Users (username, email, age, balance)"
                       f"VALUES (?, ?, ?, 1000)",
                       (username, email, age)
                       )
    else:
        print('User already exists')
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    try:
        user_check = cursor.execute(f"SELECT username FROM Users WHERE username = ?", (username, )).fetchone()
        return user_check[0] == username
    except TypeError:
        pass
    connection.commit()
    connection.close()


initiate_db()

# for i in range(4):
#     insert_products(f"Продукт {i+1}", f"*Описание {i+1}*", f"{(i+1) * 100}")


