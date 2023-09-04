# ------------------------------
# -- Strings Methods --
# ------------------------------
kunt = " Thsi is Strings "
print(kunt.center(40,"#"))

# split() rsplit()

a = "I Love Python And PHP and MYSQL"
print(a.split())

b = "I-Love-Python-And-PHP-and-MYSQL"
print(b.split("-"))

c = "I-Love-Python-And-PHP-and-MYSQL"
print(c.split("-", 3))

d = "I-Love-Python-And-PHP-and-MYSQL"
print(d.rsplit("-", 3))

# Center()

e = "Seraj"
print(e.center(9))  # spaces
print(e.center(9, "#"))  # Hashes
print(e.center(15, "@"))  # @


# count()

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP words
print(f.count("PHP", 0, 35))  # only one PHP

# swapcase
g = "I Love python"
h = "i LOVE pYTHON"
print(g.swapcase())
print(h.swapcase())

# startswith()
f = "I Love Python"
print(f.startswith("I"))
print(f.startswith("S"))
print(f.startswith("P", 7, 12))


# endswith()
j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))
