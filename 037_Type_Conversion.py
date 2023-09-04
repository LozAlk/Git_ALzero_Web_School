# -------------------------------
# -- Type Conversion --
# -------------------------------

#str()
#Tupel()
#list
# dict()



#str()
a = 10
print(type(a))
print(type(str(a)))

print("="*40)

# Tupel()

c ="Seraj" # string
d = [1,2,3,4,5] # List
e ={"A","B","C"} # Set
f = {"A":1,"B":2} # Dictionary
print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

print("="*40)

#list

c ="Seraj" # string
d = (1,2,3,4,5) # tuple
e ={"A","B","C"} # Set
f = {"A":1,"B":2} # Dictionary
print(list(c))
print(list(d))
print(list(e))
print(list(f))


print("="*40)


c ="Seraj" # string
d = (1,2,3,4,5) # tuple
e =["A","B","C"] # list
f = {"A":1,"B":2} # Dictionary
print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("="*40)

# dict()



d = (("A",1),("B",2),("C",3)) # Tuple
e =[["One",1],["Two",2],["Tree",3]] # list


print(dict(d))
print(dict(e))

