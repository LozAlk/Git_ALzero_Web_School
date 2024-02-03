# ---------------------------------------------
# -- NumPy => Compare Data Location And Type --
# ---------------------------------------------

import numpy as np

my_list = [1,2,3,4,5]
my_array = np.array([1,2,3,4,5])

print(my_list)
print(my_array)

print("#" * 40 )


print(my_list[0])
print(my_array[0])


print("+"*40)

print(id(my_list[0]))
print(id(my_list[1]))
print(id(my_array[0]))
print(id(my_array[1]))

print("@"*40)

my_list_of_Date=[1,2,"A","C",True,10.35]
my_array_of_Date =np.array([1,2,"A","C",True,10.35])

print(my_list_of_Date)
print(my_array_of_Date)
print(my_list_of_Date[0])
print(my_array_of_Date[0])
print("()"*25)
print(type(my_list_of_Date[0]))
print(type(my_array_of_Date[0]))