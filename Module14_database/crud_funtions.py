import sqlite3


connection = sqlite3.connect('products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

def insert_products(product_title, description, price):
    cursor.execute(f"INSERT INTO Products (title, description, price) VALUES(?, ?, ?)",
                   (f"{product_title}", f"{description}", f"{price}")
                   )


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    title = cursor.fetchall()
    return title

initiate_db()

# for i in range(4):
#     insert_products(f"Продукт {i+1}", f"*Описание {i+1}*", f"{(i+1) * 100}")


connection.commit()
connection.close()