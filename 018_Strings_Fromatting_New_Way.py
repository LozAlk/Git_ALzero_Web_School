# ---------------------------------
# -- Strings Formtting # --
# ---------------------------------
name = "seraj"
age = 23
rank = 10
print("my Name is: " + name)
#print("my Name is: " + name + "and My Age is: "+ age) #type Error
print("my Name is: {} " .format("seraj" ))
print("my Name is: {} and My Age is: {}".format (name, age )) 
print("my Name is: {:s} and My Age is: {:d} and My rank is: {:f}".format (name, age,rank )) 

# {:s}=> String
# {:d}=> Number
# {:f}=> float

n = "Seraj"
l = "Python"
y = 10

print("My Name is {:s} Iam {:s} Developer with {:d} Years Exp".format(n, l, y))

# Control F loating Point Number

myNumber = 10 
print("myNumber is : {}".format (myNumber)) 
print("myNumber is : {:f}".format(myNumber))
print("myNumber is : {:.5f}".format(myNumber)) 

# truncate string
mylongString  ="Hello Peoples of elzero web school i love you all"

print("Message is {:s}" .format (mylongString))
print("Message is {:.13s}".format(mylongString))


# Foemat Money 

myMoney = 50016250198
print(type("My Money in Bank Is: {}".format(myMoney)))
print("My Money in Bank Is: {:_}".format(myMoney))
print("My Money in Bank Is: {:,}".format(myMoney))

# ReArrange Items
a, b, c ="one","Two","three"
print("Hello {2} {1} {0}".format(a, b, c)) # Hello three Two one
print("Hello {0} {2} {1}".format(a, b, c)) # Hello one three Two
print("Hello {} {} {}".format(a, b, c)) # Hello one Two three

x, u, z = 10, 20, 30
print("Hello {} {} {}".format(x, u, z))
print("Hello {1:d} {2:d} {0:d}".format(x, u, z))
print("Hello {0:f} {2:f} {1:f}".format(x, u, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, u, z))

# format in version 3.6+

myName = "SERAJ"
myAge = 23
print("My Name is :{myName} and My Age is :{myAge}")
print(f"My Name is :{myName} and My Age is :{myAge}")