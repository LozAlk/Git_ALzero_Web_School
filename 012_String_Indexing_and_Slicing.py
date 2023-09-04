# -------------------------------------------
# Strings Inaexing & Slicing
# [1] All Data in python is Object
# [2] Object Contain Elements
# [3]Every Element Has Its Own Index
# [4]Python Ues Zero Based Indexing (Index Start  Form Zero)
# [5] Use Square Brachets To Access Element
# [6] Enable Accessing Parts of Strings, Tuplesor Lists
# ---------------------------------------------

# Indexing  ( Access Single Item)
mystring = "I Love Python"
print(mystring[0])  # Index 0 => I
print(mystring[9])  # Index 9 => t
print(mystring[-1])  # Index -1 => Frist character form End
print(mystring[-6])  # Index -6 => 6th character form End

# Slicing (Access Multinple Sequence Items)
# [Start:End] End Not Included
# [Start:End:Steps]
print(mystring[8:11])  # yth 
print(mystring[3:5])  # ov
print(mystring[:10])  # If start Is Not Here Will Start From 0(I Love pyt)
print(mystring[:10])  # If End Is Not Here Go To The End (e python)
print(mystring[:])  # Full Data

print(mystring[0::1])  # Full Data
print(mystring[::1])  # Full Data

print(mystring[::2])
print(mystring[::3])
