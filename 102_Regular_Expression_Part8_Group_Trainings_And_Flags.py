# ----------------------------------------------------
# -- Rrgulr Expression => Group Trainings And Flags --
# ----------------------------------------------------

import re 

my_web = "https://www.alzero.org:8080/category.php?article=105?name=how-todo"
sarech = re.search(r"(https:?)://(www)?\.?(\w+):?(\d+)?/?(.+)",my_web)

#print(dir(sarech.group))

#print(sarech.group)

#print(sarech.groups)

#for sarech in sarech.groups():
#    print(sarech)

print(f"Protocol:{sarech.group(1)}")

print(f"sub Domain :{sarech.group(2)}")

print(f"Domain Name :{sarech.group(3)}")

print(f"Top Level Domain :{sarech.group(4)}")

print(f"Port:{sarech.group(5)}")

#print(f"Query String :{sarech.group(6)}") # He needs another groupملاحضه؟ #