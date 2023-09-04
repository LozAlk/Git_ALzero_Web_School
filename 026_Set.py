# --------------------------------------
# -- Set --
# ---------
#[1] Set Items Are Enclosed in Curly Braces
#[2] Set Items Not Ordered And Not Indexed
#[3] Set Indexing and Slicing Cant Be Done
#[4] Set Has Only Immutable Data Types (Numbers, Strings,Tuples) List and Dict Are Not
#[5] Set Items Is Unique
#----------------------------------------

# Not Ordered And Not Indexed
mySetOne = {"ahmad","seraj",100}
print(mySetOne)
#print(mySetOne[0])# TypeError: 'set' object is not subscriptable


#Slicing Cant Be Done


mySetTow = {1,2,3,4,5,6}
#print(mySetTow[0:3])

# Has Only Immutable Data Types
#mySetThree = {"Seraj",100,100.5,True,[1,2,3]} # unhashable type: 'list'
mySetThree = {"Seraj",100,100.5,True,(1,2,3)}
print(mySetThree)

# Items Is Unique

mySetFour = {1,2,"Seraj","One","Osama",1}

print(mySetFour)


