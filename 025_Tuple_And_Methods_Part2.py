#-------------
# -- Tuple -- 
# ------------

# Tuple With One Element 

myTuple1 = ("seraj")
myTuple2 = "seraj"

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

print(len(myTuple1))
print(len(myTuple2))

# Tuple Concatenation
a = (1,2,3,4)
b = (5,6)

c = a + b
print(c)

p = a+("A","B", True,)+b
print(c)
print(p)

# Tuple, List, String Repear (*)

myString = "Seraj"
myList = [1,2]
myTuple = ("A","B")



print(myString* 10)
print(myList* 10)
print(myTuple* 10)

# Methods => count()

a = (1,3,3,4,5,5,5,7,8,2,6,5,8)
print(a.count(5))

# Methods => Index()

b = (1,3,7,8,2,6,5)

#print("The Position of Index Is: " + b.index(7))# Error
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"THe Position of Index Is:{b.index(7)}")

# Tuple Destruct 

a = ("A","B",4,"C")
x,y,_,z = a
print(z)
print(x)
print(y)