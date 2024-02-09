# -------------------------------------------
# -- NumPy => Arithmetic & Useful Operations 
# -------------------------------------------
# - Addition 
# - Subtraction 
# - Multiplication 
# - Divination 
# -----------------
# min
# max
# sum 
# - ravel => Returns Flattened Array 1 Dimension With Same Type 
# ---------------------------------------------------------------

import numpy as np
# Arithmetic Operations 

my_array1 = np.array([10,20,30])
my_array2 = np.array([5,2,4])

print(my_array1 + my_array2) # result [15 22 34]
print(my_array1 - my_array2) # result [ 5 18 26]
print(my_array1 * my_array2) # result [ 50  40 120]
print(my_array1 / my_array2) # result [ 2.  10.   7.5]

print("#"*40)

my_array3 = np.array([[1, 4], [5, 9]])
my_array4 = np.array([[2, 7], [10, 5]])


print(my_array3 + my_array4) # result [[ 3 11], [15 14]]
print(my_array3 - my_array4) # result [[-1 -3], [-5  4]]
print(my_array3 * my_array4) # result [[ 2 28], [50 45]]
print(my_array3 / my_array4) # result [[0.5        0.57142857], [0.5        1.8       ]]

print("#"*40)

my_array5 = np.array([10,20,30])

print(my_array5.min()) # result 10
print(my_array5.max()) # result 30
print(my_array5.sum()) # result 60
print("#"*40)

my_array6 = np.array([[2, 7], [10, 5]])
print(my_array6.min()) # result 2
print(my_array6.max()) # result 10
print(my_array6.sum()) # result 24
print("#"*40)

# Ravel 

my_array7 = np.array([[2, 7], [10, 5]])
print(my_array7.ravel())# result [ 2  7 10  5]

my_array8 = np.array([[1, 4], [5, 9]], [[2, 7], [10, 5]])

# print(my_array8.ndim) # result 2
# print(my_array8.ravel())