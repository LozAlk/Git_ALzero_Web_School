# ----------------------------
# -- Loop => While Training --
# ----------------------------
# While Condition_is_true
# Code will run Until Condeition Become False
# ------------------------------

myF = ["Os","Ah","Ga","Al","Ra","Sa","Ta","Ma","Mo","Wa"]

# print(lan(myF)) # List Length [10]

a = 0

while a < len(myF): # a < 10
    print(f"#{str(a+1).zfill(3)} {myF[a]}")

    a+=1 # a = a + 1

#print(myF[0])
#print(myF[1])
#print(myF[2])
#print(myF[4])
#print(myF[5])
#print(myF[6])
#print(myF[7])
#print(myF[8])
#print(myF[9])