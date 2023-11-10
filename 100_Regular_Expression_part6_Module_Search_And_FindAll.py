# --------------------------------------------------------
# -- Regular Expression => Re Module Search And Findall --
# --------------------------------------------------------
# Serach () => Search A String For A Match And Return A First Match Only
# Findall() => Returs A List Of All Matches and Empty List if no Match
# ---------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\(com|nat|org|info)
# --------------------------------------------------------------


import re

# my_serach = re.search(r"[A-Z]{2}","SSerajAlkherat")

#print(my_serach)
#print(my_serach.string)
#print(my_serach.span())
#print(my_serach.group())

#is_Email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|nat)", "sera@gmail.com")
#if is_Email:
#    print("This is A Valid Email ")
#    print(is_Email)
#    print(is_Email.string)
#   print(is_Email.span())
#   print(is_Email.group())


#else:
#    print("This is Not Email ")

#print(dir(re ))

email_input=input("Plese Write YOur Email ? ").strip()

serach=re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|nat",email_input)

empty_list = []

if serach != []:

    empty_list.append(serach)

    print("Email Added")

else:
    print(" Invalid Email ")

for email in empty_list: 

    print(email)



