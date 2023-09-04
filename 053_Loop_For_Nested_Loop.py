# --------------------
# -- Lopp => For --
# -- Nested Loop --
# --------------------

"""
peoples = ["Seraj","Osame","Sayed","Ail"]


skills = ["HTML","CSS","JS"]

for name in peoples:
    
    print(f"{name} Skills Is:")

    for skill in skills :
      print(f"_{skill}")
      

"""

peoples = {
        "Seraj" :{
         "HTML" : "90%",
         "Css" : "80%",
          "Js" : "70%"
        },
        "Ahmed" :{
         "HTML" : "90%",
         "Css" : "80%",
         "Js" : "60%"
        },
        "Sayed":{
         "HTML" : "90%",
         "Css" : "80%",
          "Js" : "100%"
        },
        
}
     

"""print(peoples["Seraj"])
print(peoples["Sayed"]['Css'])"""

for name in peoples :
    print(f"Skills and Porgress For {name} Is .")

    for skill in peoples[name]:

        print(f"{skill.upper()} => {peoples[name][skill]}")