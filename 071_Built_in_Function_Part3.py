# ---------------------------------
# -- Built in function --
# -----------------------
# abs()
# pow()
# min()
# max()
# silce()
# ------------------------


#abs()
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))
print("="*40)

# pow(base,exp,mod) => Power
print(pow(2,5)) # 2 * 2 * 2 * 2 * 2
print(pow(2,5,10)) # (2 * 2 * 2 * 2 * 2)%10

print("="*40)

# min(item,itme,itme,or iterator)
myNumbers = (1,20,-50,-100,100)
print(min(1,10,-50,100))
print(min("A","X","Z","Seraj"))
print(min(myNumbers))

print("="*40)

# max(item,itme,itme,or iterator)
myNumbers = (1,20,-50,-100,100)
print(max(1,10,-50,100))
print(max("A","X","Z","Seraj"))
print(max(myNumbers))

print("="*40)

# silce(start,end,step)
a = ["A","B","C","D","E","F"]
print(a[:])
print(a[slice(5)])
print(a[slice(2,5)])
print(a[2:5])