#   ------------------------------------
# -- Lists Methods --
#   -----------------------------------
# 
# #append 

myFriends = ["Seraj", "Lolo","Momo"]
myOfsriend = ["Sadam", "Lilan","Soso"]
myFriends.append("Mhmmod")
myFriends.append(100)
myFriends.append(100.500)
myFriends.append(True)
myFriends.append(myOfsriend)

print(myFriends)
print(myFriends[3])
print(myFriends[6])
print(myFriends[7][2])
print("="*40)
# extend()

a = [1,2,3,4]
b =["A","B","C"]
c =["One","Tow"]
a.extend(b)
a.extend(c)
print(a)
print("="*50)

# remove()
x =[1,2,3,4,5, "srag", True, "srag","srag"] 
x.remove("srag")
x.remove("srag")
print(x)
print("="*50)
#sort
y = [1,2,100,120,-10,17,29]
y.sort(reverse=False)
# y.sort(reverse=True)
print(y)
print("="*50)
# revese()
z =[10, 1, 9, 80, 100, "Srag",100]
z.reverse()
print(z)
