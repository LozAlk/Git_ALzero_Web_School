import sqlite3

db = sqlite3.connect("app.db")
cr = db.cursor()
uid = 2

# # تعريف الجدول إذا لم يكن موجودًا
# cr.execute('''
#     CREATE TABLE IF NOT EXISTS skills (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         progress TEXT NOT NULL,
#         user_di INTEGER NOT NULL,
#         FOREIGN KEY (user_di) REFERENCES users (id) 
#     )
# ''')

def commit_and_close():
    """Commit Changes and Close Connection To Database"""
    db.commit()
    db.close()
    print("Connection to Database Is Closed")

input_message = """
What Do You Want To Do?
"s" => Show All Skills
"a" => Add New Skill 
"d" => Delete A Skill Progress
"u" => Update Skill Progress
"q" => Quit The App 
Choose Option
"""

# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List
commit_list = ["s", "a", "d", "u", "q"]

# Define The Methods
def show_skills():
    cr.execute("select * from skills ")

    reults = cr.fetchall()

    print(f"YOu Have {len(reults)} Skills.")

    print("Shwing Skills Whit Porgress:")

    if len(reults) > 0:

        print("Showing Skills whit progress: ")

    for row in reults:

        print(f"Skill => {row[0]}",end=" ")

        print(f"Porgress => {row[1]}")


    commit_and_close()

def add_skills():
    sk = input("Write Skill Name: ").strip().capitalize()
    prog = input("Write Skill Progress: ").strip()
    cr.execute(f"INSERT INTO skills(name, progress, user_di) VALUES ('{sk}', '{prog}', '{uid}')")
    commit_and_close()

def delete_skills():
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"DELETE FROM skills WHERE name = '{sk}'")
    commit_and_close()

def update_skills():
    print("Update Skill Progress")

# Check If Command Is Exists
if user_input in commit_list:
    print(f"Command Found: {user_input}")

    if user_input == "s":
        show_skills()

    elif user_input == "a":
        add_skills()

    elif user_input == "d":
        delete_skills()

    elif user_input == "u":
        update_skills()

    else:
        print("App Is Closed.")
        commit_and_close()

else:
    print(f"Sorry, This Command \"{user_input}\" Is Not Found")
    