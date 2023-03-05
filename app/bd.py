import sqlite3

connect = sqlite3.connect("app/app.db")
print('Created')

cursor = connect.cursor()
cursor.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, password TEXT)""")
connect.commit()
print('Table Created')
