# --------------------
# -- Strings Methods --
# --------------------

# Strip() rstrip() lstrip()
# print(len(a.lstrip()))

a = "    I love python    "
print(a.strip())
print(a.rstrip())
print(len(a.lstrip()))
a = "#####I love python######"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

# title()

a = "I love 2d Graphics and 3g technology and python"
print(a.title())

# capitalize()
b = "I Love 2D Graphics And 3G Technology And Python"
print(b.capitalize())

# zfill

c, d, e, f = "1", "11", "111", "1111"
print(d)
print(c)
print(d)
print(f)

print(c.zfill(3))
print(c.zfill(3))
print(c.zfill(3))
print(c.zfill(3))

# upper()
g = "SERAJ"

print(g.upper())

# lower()

print(g.lower())
