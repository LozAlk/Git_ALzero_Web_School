# ---------------------------------------
# -- Built In Function => Map --
# ------------------------------

# [1] Map Taek A Function + Iterator '
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Functio
# ---------------------------------------------------------------

print("#"*80)
print('-- Built In Function => Map -- '.center(80,"#"))
print('#'*80)


# Ues Map With Predefined Function 

def formatText(text):

    return f"- {text.strip().capitalize()}. -"

myTexts = ["Seraj","AHMED","Alkerat"]

#myFormatedData = map(formatText,myTexts)

#print(myFormatedData)

for name in list(map(formatText,myTexts)):

    print(name)

print("="*40)

# Ues Map With Lambda Function 

#def formatText(text):

#    return f"- {text.strip().capitalize()}. -"
  
myTexts = ["Seraj","AHMED","Alkerat"]

#myFormatedData = map(formatText,myTexts)

#print(myFormatedData)

for name in list(map(lambda text:f"- {text.strip().capitalize()}. -",myTexts )):

    print(name)



print("#"*80)
print(' Ok Dank je Veel '.center(80,'#'))
print("#"*80)