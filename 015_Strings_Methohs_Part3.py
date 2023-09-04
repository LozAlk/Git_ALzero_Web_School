 # ---------------------------
# -- Strings Methods --
# ---------------------------

# index(SubStrings, Start, End)



a = "I Love Python"
#print(a.index("P")) # Index Number 7
#print(a.index("P", 0, 10))# Index Number 7 
#print(a.index("P", 0, 5)) # Through Error

# find(SubStrings, Start, End)
b = "I Love Python"
print(b.find("P")) # Index Number 7
print(b.find("P", 0, 10))# Index Number 7 
print(b.find("P", 0, 5)) # -1

#rjust(width, fill char) ljust(width, fill char)
c = "Seraj"
print(c.rjust(10))
print(c.rjust(10,"#"))


d = "Seraj"
print(d.ljust(10))
print(d.ljust(10,"#"))

# Splitlines()
e = """first line
second line
third line"""
print(e.splitlines())

f = "Frist line\nsecond line \nthinr line"
print(f.splitlines())
# expandtads()
g = "Hello\tWorld\tI\tLove\tPython"
#print(g.expandtads(20))

one ="I Love Python And 3G"
tow =("i love Python and 3g")
print(one.istitle())
print(tow.istitle())

three = " "
fore = ""
print(three.isspace())
print(fore.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower)
print(six.islower)

seven = "seraj_alkherat"
eigth = "SerajKalherat1000"
nine = "Seraj--Kalherat1000"
print(seven.isidentifier())
print(eigth.isidentifier())
print(nine.isidentifier())

x ="AaaaaaaaBbbbbbb"
y ="AaaaaaBbbbbbbb11"
print(x.isalpha())
print(y.isalnum())