# -*- coding: utf-8 -*-
"""Pandas DB connection sqlite3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tauwepDUQwMVKhG4g06NuVb0I-OPw8Na
"""

!pip install pandas

!pip install pysqlite3

import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

conn.commit()

cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 25))
conn.commit()

#data to insert
data = [
   ('Murali', 28),
   ('Sangu', 28),
   ('Sujji', 25)
]
#Inser Multiple rows
cursor.executemany('''
INSERT INTO users (name, age)
VALUES(?, ?)
''', data)
conn.commit()

import pandas as pd
df = pd.read_sql_query('SELECT * FROM users', conn)
print(df)

update_data = [
   (25, 'Murali'),
   (26, 'Alice')
]
cursor.executemany('''
update users
set age = ?
where name = ?
''', update_data)
conn.commit()

# Filtering data
filtered_df = df[df['age'] > 20]

# Grouping data
grouped_df = df.groupby('age').count()