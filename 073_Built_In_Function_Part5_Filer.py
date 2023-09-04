# ----------------------------------
# -- Built In Function => Filtern --
# ----------------------------------
# [1] Filter Take A Function + Iterator 
# [2] Filter Run A Function on Every Element 
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Element For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ----------------------------------------------------------------

# Example 1

def checkNumber(num):
    
        return num > 10
    
myNumbers =[0,0,1,10,19,20,100,5]

myResult = filter(checkNumber,myNumbers)

for number in myResult:

    print(number)

print("="*49)

# Example 2

def checkName(name):

    return name.startswith("S")

myTexts =("Serag","Soso","Sedra","Ahmad")

myReturnedata = filter(checkName,myTexts)

for name in myReturnedata:
     
     print(name)

print("="*49)
# Example 3 

#def checkName(name):
#     return name.startswith("S")

myNames = ["Serag","Soso","Sedra","Ahmad","Othman","Omar","Ameer"]
 
for p in filter(lambda name: name.startswith("S"),myNames):
     print(p)