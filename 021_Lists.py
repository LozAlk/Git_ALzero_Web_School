# -------------------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data T Ypes
# --------------------------------------

myAwesomeList = ["one", "Tow", "One", 1, 100.5, True]
print(myAwesomeList) #Whole List
print(myAwesomeList[1])#  Tow
print(myAwesomeList[-1])# True
print(myAwesomeList[-3]) # 1


print(myAwesomeList[1:4]) # ['Tow', 'One', 1]
print(myAwesomeList[:4]) # ['one', 'Tow', 'One', 1]
print(myAwesomeList[1:]) # Tow', 'One', 1, 100.5, True]
print(myAwesomeList[::1])# ['one', 'Tow', 'One', 1, 100.5, True]
print(myAwesomeList[::2]) #['one', 'One', 100.5]

print(myAwesomeList)
myAwesomeList[1]  = 2 # ['one', 2, 'One', 1, 100.5, True]
myAwesomeList[-2] = 2 # ['one', 2, 'One', 1, 2, True]
myAwesomeList[-1] = False




