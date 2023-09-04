# ---------------------
# -- Functino Scope --
# ---------------------

#x = 1 # Global Scope 

def one():
    global x
    x=2
    print(f"Print Variable From Golbal Scope {(x)}")
def two():
    x=10
    print(f"Print Vaiable From Function {x}")
def Thry():
        x=13
        print(f"Print Varilable Form golbal Scope {x}")



one()
print(f"Print Variable From Function Scope {x}")

two()
print(f"Print Variable Form Function Scope After Ome function Is Called {x}")

Thry()
print(f"Print Vairable Form Scope Function {x}")