# -------------------------
# -- Boolean Operators --
# -------------------------
# and
# or
# Not
# -------------------------

age = 23
country = "Egypt"
rank = 10
print(age > 16 and country == "Egypt" and rank > 0) # True
print(age >16 and country == "KAS" and rank > 0) # False

print("#"*40)


print(age > 40 or country == "KSA" or rank > 40)# False
print(age > 40 or country == "Egypt" or rank > 20) # True

print("#"*40)

print(age>16) # True
print(not age >16)#Not True = False