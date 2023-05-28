import sqlite3


connection = sqlite3.connect('testingDB.db')
cursor = connection.cursor()

# cursor.execute('create table products(name, description, price)')
cursor.execute("""
    insert into products values
        ('Product 1', 'Description 1', '23.54'),
        ('Product 2', 'Description 2', '52.12'),
        ('Product 3', 'Description 3', '78.42')
""")
connection.commit()


print(cursor.execute('select name from products').fetchall())