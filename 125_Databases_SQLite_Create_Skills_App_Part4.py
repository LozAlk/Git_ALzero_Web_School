import sqlite3

# Connect to the database
db = sqlite3.connect("app.db")
cr = db.cursor()
uid = 2  # Define the user ID

# Define the table if it does not exist
cr.execute('''
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        progress TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id) 
    )
''')

# Define the users table if it does not exist
cr.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Function to commit changes and close the database connection
def commit_and_close():
    """Commit Changes and Close Connection To Database"""
    db.commit()
    db.close()
    print("Connection to Database Is Closed")

# Function to show user information
def show_user_info():
    cr.execute("SELECT name FROM users WHERE id = ?", (uid,))
    user_name = cr.fetchone()

    if user_name:
        print(f"User Information for user_id {uid}:")
        print(f"User Name: {user_name[0]}")
    else:
        print(f"User with user_id {uid} not found.")

# Function to show skills
def show_skills():
    cr.execute("SELECT * FROM skills WHERE user_id = ?", (uid,))

    results = cr.fetchall()

    print(f"You Have {len(results)} Skills.")

    print("Showing Skills With Progress:")

    if len(results) > 0:
        print("Showing Skills with progress: ")

    for row in results:
        print(f"Skill => {row[1]}", end=" ")
        print(f"Progress => {row[2]}")

    commit_and_close()

# Function to add a new skill
def add_skills():
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"SELECT name FROM skills WHERE name = ? AND user_id = ?", (sk, uid))
    results = cr.fetchone()
    if results is not None:
        print("Skill Exists. You Cannot Add It :)")
    else:
        prog = input("Write Skill Progress: ").strip()
        cr.execute("INSERT INTO skills(name, progress, user_id) VALUES (?, ?, ?)", (sk, prog, uid))
        commit_and_close()
        print(f"Skill '{sk}' added successfully!")

# Function to delete a skill
def delete_skills():
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute("DELETE FROM skills WHERE name = ? AND user_id = ?", (sk, uid))
    commit_and_close()
    print(f"Skill '{sk}' deleted successfully!")

# Function to update skill progress
def update_skills():
    sk = input("Write Skill Name: ").strip().capitalize()

    prog = input("Write The New Skill Progress: ").strip()

    cr.execute("UPDATE skills SET progress = ? WHERE name = ? AND user_id = ?", (prog, sk, uid))
    
    commit_and_close()
    print(f"Skill '{sk}' progress updated successfully!")

# Message for choosing an option
input_message = """
What Do You Want To Do?
"s" => Show All Skills
"a" => Add New Skill 
"d" => Delete A Skill Progress
"u" => Update Skill Progress
"v" => View User Information
"q" => Quit The App 
Choose Option
"""

# Choose an option
user_input = input(input_message).strip().lower()

# List of possible commands
commit_list = ["s", "a", "d", "u", "v", "q"]

# Check if the command exists
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

    elif user_input == "v":
        show_user_info()

    else:
        print("App Is Closed.")
        commit_and_close()
        print("Thank you for using the app. You're beautiful!")

else:
    print(f"Sorry, This Command \"{user_input}\" Is Not Found")
