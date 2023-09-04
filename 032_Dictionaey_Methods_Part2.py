# -----------------------------------
# -- Dictionary Methods --
# -------------------------


# setdefault()

user = {
    "name" : "Seraj"
}
print(user)
print(user.setdefault("age",23))
print(user)

print("="*40)

# popitem()

member = {
    "name":"Seraj",
    "skil":"PS3"
}
print(member)
member.update({"age" : 23})
print(member.popitem())

print("="* 40)


# items()

view = {
    "name" : "Seraj",
    "sikll" : "XBox"
}

allItems = view.items()
print(view) 
view ["age"] = 23
print(allItems)

print("="*40)

# fromkeys()

a =('MYkeyOne', 'MYkeyTwo','MYkeyThree')
b = "X"

print(dict.fromkeys(a, b))