# ------------------------
# -- Control Flow   --
# -- If, Elif, Else --
# -- Make Decisions --
# ------------------------


uName = input('wat is name ? ')
uCountry = input(' Your are from ?')
cName = "Python Course"
cPrice = 100

#cDiscount = 30
if uCountry == "Egypt":
     
     print(f" Hello {uName} Because You Are From {uCountry}")
     print(f" The Course\"{cName}\" Price Is : $ {cPrice - 80 }")

elif uCountry == "KSA":

     print(f" Hello {uName} Because You Are From {uCountry}")
     print(f" The Course\"{cName}\" Price Is : $ {cPrice - 60 }")

elif uCountry == "Kuwait":

     print(f" Hello {uName} Because You Are From {uCountry}")
     print(f" The Course\"{cName}\" Price Is : $ {cPrice - 60 }")

else :
         
     print(f" Hello {uName} Because You Are From {uCountry}")
     print(f" The Course\"{cName}\" Price Is : $ {cPrice - 70 }")