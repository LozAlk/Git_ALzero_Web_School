# ---------------------------------------
# -- Ternary Conditional Operator --
# ---------------------------------------



country ="KSA"

if  country == "Egypt":
     print(f"The Weather in {country} Us 15")
elif country == "KSA":
     print(f"The Weather in {country} Us 30")
else :
     print("Country is Not inthe List")
    
# Short If 

moiveRate = 18
age = 16

if age < moiveRate :
    print("Movie S Not Good 4U") # Condition If True

else :
    print("movies S Good 4U And Happy Watching") # Condition If False

print("Movies s Good 4U" if age < moiveRate else "movies S Good 4U And Happy Watching")

# Condition if True | if condition | Else | condition if False