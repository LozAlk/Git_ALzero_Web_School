# ----------------------------
# -- Set Methods --
# ---------------------------


# issuperset()

a = {1,2,3,4,}
b = {1,2,3}
c = {1,2,3,4,5}
print(a.issuperset(b)) # True
print(a.issuperset(c)) # False

print("=" * 40)

# issubset()

d = {1,2,3,4}
e = {1,2,3}
f = {1,2,3,4,5}

print(d.issubset(e)) # False
print(d.issubset(f)) # True

print("=" * 40)

# isdisjoint

g = {1,2,3,4}
h = {1,2,3}
i = {10,11,12}
print(g.isdisjoint(i)) # True
print(g.isdisjoint(h)) # False
