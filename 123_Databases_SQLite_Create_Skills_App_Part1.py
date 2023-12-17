# -----------------------------------------------------
# --  Databases => SQLite => Create Skills App Part1 --
# -----------------------------------------------------
input_message = """
what Do you Want To De ?
"s" => Show All Skills
"a" => Add New Skill 
"d" => Delete A Skill Progress
"u" => Update Skill Porgress
"q" => Quit The App 
Choose Option
"""


# Input Option Choose
user_input = input(input_message).split()

# Command List
commit_list = ["s","a","d","u","q"]


# Define The Methods


def show_Skils():
    print("Show All Skills")

def add_Skills():
    print("Add New Skill")

def delete_Skills():
    print("Delete A Skill Progrress")

def update_Skills():
    print("Update Skill Porgress")


# Check If Command Is Exists
if user_input in commit_list:
    print(f"Command Found {user_input}")

    if user_input == "s":
        show_Skils()

    elif user_input == "a":
        add_Skills()

    elif user_input == "d":
        add_Skills()

    elif user_input == "u":
        
        update_Skills()

    else:
        print("App Is Closed.")
        


else:
    print(f"Sorry This Command \"{user_input}\" Is Not Found")