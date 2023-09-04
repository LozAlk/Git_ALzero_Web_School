# -----------------------
# -- Built In Function --
# -----------------------
# enumerate ()
# help()
# reversed()
# -----------------------

# enumerate (iterable, start=0)

mySkils = ["Html","Css","Js","PHP"]

myskilswithcounter = enumerate(mySkils,20)

print(type(myskilswithcounter))

for c,s in myskilswithcounter :

    print(f"{c} - {s}")

print("="*49)

# help()

#print(help(print))

print("="*49)

# reversed()

myString = "Alkherat"

for letter in myString :
    print(letter)

for s in reversed(mySkils):
    print(s)


print( 'The END'.center(80,"#"))

