# -----------------------------------------
# -- NumPy => Data Types And Control Array 
# -----------------------------------------
# https://numpy.org/devdocs/user/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arryas/dtypes.html#specfying-and-constructing-data-type
# ----------------------------------------------
# '?' boolean
# 'b' (signed) byte
# 'B' unsigned byte
# 'i' (signed) integer
# 'u' unsigned integer 
# 'f' floating-point
# 'c' complex-floating point
# 'm' timedelta 
# 'M' datetime
# 'O' (Python) Objects
# 'S','a' zero-terminated bytes (not commended)
# 'U' Unicode string
# 'V' raw date (void)
# ------------------------------------------------

import numpy as np

# Show Array Data Type

my_array1 = np.array([1,2,3])
my_array2 = np.array([1.5,20.15,3.601])
my_array3 = np.array(["Seraj","B","Ahmed"])

print(my_array1.dtype)
print(my_array2.dtype)
print(my_array3.dtype)

print("#"*40)

# Create Array With Specific Data Type


my_array4 = np.array([1,2,3],dtype=float) # float or 'float' or 'f'
my_array5 = np.array([1.5,20.15,3.601],dtype=int) # int or 'int' or 'n'
#my_array6 = np.array(["Seraj","B","Ahmed"],dtype=int) # Value Error

print(my_array4.dtype)
print(my_array5.dtype)
#print(my_array6.dtype)

print("#"*40)

# Change Data Type Of Existing Array

my_array7 = np.array([0,1,2,3,0,4])
print(my_array7.dtype)
print(my_array7)

print("#"*40)

my_array7 = np.array([0,1,2,3,0,4],dtype=bool)
print(my_array7.dtype)
print(my_array7)

print("#"*40)

my_array7 = np.array([0,1,2,3,0,4],dtype=float)
print(my_array7.dtype)
print(my_array7)

print("#"*40)

# Test Capacity

my_array8 = np.array([100,200,300,400],dtype='f')
print(my_array8.dtype)
print(my_array8[0].itemsize) # 4 Bytes 
print("#"*40)
my_array8=my_array8.astype('float') # Change To Float64
print(my_array8.dtype)
print(my_array8[0].itemsize)