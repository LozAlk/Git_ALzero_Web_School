# ------------------------------------------------------
# -- Databases => SQLite => Insert Data Into Database --
# ------------------------------------------------------
# - Cursor => All Operation in SQL Done By Cursor Not Connection Itself 
# - commit => Save All Changes 
# -------------------------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And (Connect)
db= sqlite3.connect('app.db')

# Setting Up The Cursor 
cr = db.cursor()


# Create The Tabbles and Fields
cr.execute("create table if not exists users (user_id integer, name text)")
cr.execute("create table if not exists skills (name text,progress integer, user_id integer)")

# Inserting Data 

# cr.execute("insert into users(user_id,name) values(1,'Seraj')")
# cr.execute("insert into users(user_id,name) values(1,'Alkherat')")
# cr.execute("insert into users(user_id,name) values(1,'Famle')")


my_list =['Seraj','Alkherat','Ali','Sameh','Kamel','Enas']

for key,user in enumerate(my_list):
    cr.execute(f"insert into users(user_id,name) values({key+1}, '{user}')")


# Save (commit) Changes
db.commit()

# Close Database 
db.close()
