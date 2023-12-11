# --------------------------------------------------------
# -- Databases => SQLite => Retrieve Data From Database --
# --------------------------------------------------------
# - fetchone => returns a single recode or None if more rows are available.
# - fetchall => fetches all the rows of a query result. it returs all the rows
#                     as a list of tuples.An empty list is returned if there is on record to Fetch.
# - fetchmanu(size) =>
# -------------------------------------------------------------------------------
# Import SQLite Module 
import sqlite3

# create Database And Connect 
db = sqlite3.connect("app.db")

cr=db.cursor()

# Create the Tables and Fields 
cr.execute('create table if not exists users (user_id integer, name text)')
cr.execute('create table if not exists skills (name text,progerss integer,user_id integer)')



# Inserting Data
# cr.execute('insert into users(user_id ,name) values(1,"seraj")')
# cr.execute('insert into users(user_id ,name) values(1,"hamed")')
# cr.execute('insert into users(user_id ,name) values(1,"alkherat")')



cr.execute("select * from users")

#print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
#print(cr.fetchall())
#print(cr.fetchmany(2))



# Save (Commit ) Changes

db.commit()

# Close Database
db.close()