# ---------------------------------
# -- Modules => Create Your Module --
# ---------------------------------


#import sys 
#sys.path.append(r"c:\Program")
#print(sys.path)


#import Alkherat as a
#print(dir(Alkherat))

#a.sayHello("Seraj")
#a.sayHello("Ahmad")
#a.sayHello("Lolo")

#a.sayHowAreYou("Seraj")
#a.sayHowAreYou("Ahmad")
#a.sayHowAreYou("Sedra")

# Alias
"""
import Alkherat 
#print(dir(Alkherat))

Alkherat.sayHello("Seraj")
Alkherat.sayHello("Ahmad")
Alkherat.sayHello("Lolo")

Alkherat.sayHowAreYou("Seraj")
Alkherat.sayHowAreYou("Ahmad")
Alkherat.sayHowAreYou("Sedra")
"""

from Alkherat import sayHello as s
s("Seraj")