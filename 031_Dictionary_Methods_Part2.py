# --------------------------
# -- Dictionary Methods -- 
# --------------------------

# clear()


user = {
    "name" : "Seraj"
}

print(user)
user.clear()
print(user)

print("="*40)

# update()

member = {
    "name" : "Seraj"
}
print(member)
member["age"]=21
print(member)
print("="*50)

# copy()

main = {
    "name" : "Seraj"
}
b =main.copy ()

print(b)
main.update({"skills":"fighting"})
print(main)
print(b)

# keys()+ values()
print(main.keys())
print(main.values())