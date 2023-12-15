# --------------------------------------------
# -Databases => SQLite => Update and Delete --
# --------------------------------------------



# Imoprt SQLite Module 
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()


# cr.execute("update users set name = 'Mahomd' where user_di = 1")
# cr.execute("update users set name = 'alkherat' where user_di = 2")
# cr.execute("update users set name = 'Ahmad' where user_di = 3")

# Delete Data
#cr.execute("delete from users where user_di = 4")

# Fetch Data
#cr.execute("select * from users")


print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# Save (Commit) Changes 
db.commit()

# Close Database
db.close()