# ----------------------------
# -- NumPy => Create Arrays --
# ----------------------------

import numpy as np

my_list = [1,2,3,4,5]
my_array = np.array(my_list)

print(my_list)
print(my_array)

print("#" * 50)

a = np.array(10)
b = np.array([10,20])
c = np.array([[1,2],[3,4]])
d = np.array([[[5,6],[7,9]],[[1,3],[4,8]]])

print(d[1][1][1])
print(d[1,1,1])
print(d[1,1,-1])

print("#"*40)
# Number Of Dimensions

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("#"*40)
# Custom Dimensions 

my_custom_array = np.array([1,2,3],ndmin=3)

print(my_custom_array)
print(my_custom_array.ndim)
print(my_custom_array[0,0,0])