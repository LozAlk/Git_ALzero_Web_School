# --------------------------------------
# -- Tuple --
#--------------
# [1] Tuple Item Are Enclosed in parentheses
# [2] You Can Remove The Parentheses
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Usrd in Strings and Lists Availadlr In Tuples
# ---------------------------------------

# Tuple Syntax & Type Test

mySerajTupleOne = ("Seraj","Ahmad")
mySerajTupleTwo= "Seraj","Ahmad"
print(mySerajTupleOne)
print(mySerajTupleTwo)

print("="*40)

print(type(mySerajTupleOne))
print(type(mySerajTupleTwo))

print("="*40)

# Tuple Indexing
mySerajTupleThree =(1,2,3,4,5)
print(mySerajTupleThree[0])
print(mySerajTupleThree[-3])
print(mySerajTupleThree[-1])

print("="*40)

# Tuple Assign Values
mySerajTupleFour = (1,2,3,4,5)
#mySerajTupleFour[2] = "three" #TypeError: 'tuple' object does not support item assignment
print(mySerajTupleFour)

print("="*40)

# Tuple Items

mySerajTupleFive = ("Seraj", "Ahmad",1,2,3,100.5,True)
print(mySerajTupleFive[1])
print(mySerajTupleFive[-1])

print("-"*40)
