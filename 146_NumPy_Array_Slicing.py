# ----------------------------
# -- NumPy => Array Slicing --
# ----------------------------


import numpy as np


# Slicing => [Start:End:Steps] Not Including End

a = np.array(["A","B","C","D","E","F"])


print(a.ndim)
print(a[1])
print(a[1:4])
print(a[:4])
print(a[2:])


print("#"* 40)

b=np.array([["A","B","Z"],["C","D","Y"],["E","F","Z"],["M","N","O"]])

print(b.ndim)
print(b[1])
print("#"*40)

print(b[:3])
