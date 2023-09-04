# -------------------------------
# -- Dictionary --
# -----------------
# [1] Dict Item Are Enclosed in curly Braces 
# [2] Dict Item Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Nuber, String, Tuple) List Not Alloewd
# [4] Dict Key Value Can Have Any Data Types 
# [5] Dict Key Need TO BE Unique
# [6] Dict Is Not Ordered You Access Its Elmemnt With Key
# --------------------------------

# Dictinary

user ={
     "name"   : "Seraj",
     "age"    :  "23",
     "country": "Egypt",
     "skills" :["Html", "Css","Js"],
     "rating" : 10.5
     
}
print(user)
print(user["country"])

print(user.keys())
print(user.values())

print("="*40)

#Two_Dimensioal_Dictionary

languages = {
    "One" :{
        "name":"HTML",
        "porgress" : "80%"
    },
    "Two" :{
       " name":"Css",
       "porgress" : "90%"
    },
    "Three" :{
        "name" : "JS",
        "porgress" : "90%"
    }
}

print(languages)

print("=" * 40)

print(languages['One'])
print(languages["Three"]['name'])

print("-"*40)

# Dictionary Length
print(len(languages))
print(len(languages["Two"]))
print("="*40)
#  Create Dictionary From Variables

frameworkOne ={
    "name" : "Reactjs",
    "porgress":"80%"
}

frameworkTwo ={
    "name" : "Reactjs",
    "porgress":"80%"
}

frameworkThree ={
    "name" : "Reactjs",
    "porgress":"80%"
}

allframework ={
    "One" : frameworkOne,
    "Two" : frameworkTwo,
    "Three" : frameworkThree
}

#print(type(allframework))
print((allframework))
print(len(allframework))