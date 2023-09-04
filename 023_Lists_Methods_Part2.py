#   ------------------------------------
# -- Lists Methods --
#   ------------------------------------

# clear()
a = [1, 2, 3, 4]
a.clear()
print(a)

print("="*50)

# copy()
b = [1,2,3,4]
c = b.copy()
print(b) # Main List
print(c) #Copied List

b.append(5) # [1, 2, 3, 4, 5]

print(b) # Main List
print(c) # Copied List

print("="*50)

#count()
d = [1,2,3,4,3,9,10,1,2,1]
print(d.count(1))

print("="*50)

#index()
e = ["osama", "ahmed","sayed","Ramy","Ahmed","Ramy"]
print(e.index("Ramy"))

print("="*50)

#insert()

f = [1,2,3,4,5,"A","B","C"]
f.insert(0,"Tast")
f.insert(-1,"Tast")
print(f)

print("="*50)

#pop()

g =[1,2,3,4,5,"A","B",]
print(g.pop(-3))