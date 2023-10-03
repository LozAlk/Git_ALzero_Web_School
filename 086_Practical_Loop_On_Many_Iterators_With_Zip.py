# --------------------------------------------------
# -- Practical => loop on many iterators with zip --
# --------------------------------------------------
print( " Practical => loop on many iterators with zip ".center(80,"#"))

list1 =[1,2,3,4,5]
list2 =["A","B","D"]
tuple1 =("msn","womne","gilr","boy")
dich1={"name":"seraj","Age":"22","country":"d.e.z","Skils":"Python"}

for items1,items2,items3,items4 in zip(list1,list2,tuple1,dich1):
    print("list 1 Itme =>",list1)
    print("list 2 Itme =>",list2)
    print("tuple 1 Itme =>",tuple1)
    print("sich 1 Itme =>",dich1,"Value =>",dich1[items4])

#ultimelist =zip(list1,list2)
#print(ultimelist)
# for item in ultimelist:
#     print(itme)


print(" The END Code ".center(40,"#"))