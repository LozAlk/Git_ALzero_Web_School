# ------------------------------
# -- Set Methodas --
# ------------------------------


# difference()


a = {1,2,3,4,}
b = {1,2,3,"Seraj","Rooz"}
print(a)
print(a.difference(b)) # a-b
print(a)

print("=" * 40) # Separator

# difference_update()
c = {1,2,3,4,}
d = {1,2,"Seraj","Rooz"}
print(c)
c.difference_update(d) # c-d
print(c)

print("=" * 40) # Separator

# intersection()

e = {1,2,3,4,"X"}
f ={"Seraj","X",2}
print(e)
print(e.intersection(f)) # e & f
print(type(e))

print("=" * 40) # Separator

# intersection_update()

j = {1,2,3,4,"X","Seraj "}
l ={"Seraj","X",2}
print(j)
print(j.intersection_update(l)) #  j & l
print(j)

print("="*40)  # Separator

# symmetric_difference()
i = {1,2,3,4,5,"X"}
o ={"Seraj","Rooz",1,2,4,"X"}
print(i)
print(i.symmetric_difference(o)) # i | o
print(i)

print("="*40) # Separator

# symmetric_difference_update()
w = {1,2,3,4,5,"X"}
u ={"Seraj","Rooz",1,2,4,"X"}
print(w)
print(w.symmetric_difference_update(u)) 
print(w)
print("="* 40) # Separator