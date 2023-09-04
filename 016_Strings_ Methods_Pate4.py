# --------------------------------
# -- Strings Methods --
# --------------------------------

# replace (Old Value, New Vlaue, Count)

a ="Hello One Two Three One One"
print(a.replace("One","1"))
print(a.replace("One","1",1))
print(a.replace("One","1",2))

# join(Iteradle)

myList =["sreaj", "ahmad", "mohmad"]
print("-". join(myList))
print(" ". join(myList))
print(",". join(myList))
print(type("-". join(myList)))