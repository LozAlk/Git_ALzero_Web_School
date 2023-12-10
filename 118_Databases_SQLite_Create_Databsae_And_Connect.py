import sqlite3


db = sqlite3.connect('app.db')

db.execute('create table if not exists  skills (name text, progress integer, user_di integer)')


db.close()