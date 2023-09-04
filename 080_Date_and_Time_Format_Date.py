# -----------------------------------
# -- Date and time  => Format Date --
#------------------------------------ 
# -- https://strftime.oge/ --
# ---------------------------

import datetime
#print(dir(datetime.datetime))
myBirthday = datetime.datetime(2001,1,15)
print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))
print("#"*50)
print(myBirthday.strftime("%d %B %Y"))
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
print(myBirthday.strftime("%d - %B - %Y"))
print(myBirthday.strftime(" %B - %Y"))