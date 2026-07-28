# Day 63 - 100 Days of Code

import sqlite3

print(f'\n---- Structured ^ Queries ----\n')

db = sqlite3.connect('book_collection.db')
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY, 
        title varchar(250) NOT NULL UNIQUE, 
        author varchar(250) NOT NULL, 
        rating FLOAT NOT NULL
        )
''')

cursor.execute('''
    INSERT INTO books VALUES(
        1, 
        'Harry Potter', 
        'J. K. Rowling', 
        '9.3'
        )
''')

db.commit()

db.close()