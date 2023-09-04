# ---------------------------------
# -- Strings Formtting # --
# ---------------------------------
name = "seraj"
age = 23
rank = 10
print("my Name is: " + name)
#print("my Name is: " + name + "and My Age is: "+ age) #type Error
print("my Name is: %s " % "seraj" ) 
print("my Name is: %s and My Age is: %d" % (name, age )) 
print("my Name is: %s and My Age is: %d and My rank is: %f" % (name, age,rank )) 

# %s=> String
# %d=> Number
# %f=> float

n = "Seraj"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer with %d Years Exp" %(n, l, y))

# Control F loating Point Number

myNumber = 10 
print("myNumber is : %d" % myNumber) 
print("myNumber is : %f" % myNumber) 
print("myNumber is : %.2f" % myNumber) 

# truncate string
mylongString  ="Hello Peoples of alkherat web school i love you all"

print("Message is %s" % mylongString)
print("Message is %.5s" % mylongString)
