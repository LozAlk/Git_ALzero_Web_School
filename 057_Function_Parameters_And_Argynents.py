# ----------------------------------------
# -- Function Parameters And Arguments --
# ----------------------------------------

#a, b, c = "Seraj", "Ahmed", "Kherat" 


#print(f"Hello {a}")
#print(f"Hello {b}")
#print(f"Hello {c}")

# def                     => function Keyword[Define]
# Say_hello               => function Name
# name                    => Parameter
# print(f"Hello {name}")  => Task
# say_hello("Ahmed")      => Ahmed Is The Argument

#def say_hello(n):

#    print(f"Hello {n}")

#say_hello(a)
#say_hello(b)
#say_hello(c)


#def addition(n1, n2):
#    print(n1 + n2)

#addition(100,50)
#addition(-50,90)
#addition(-50,100)

def addition(n1, n2):
    if type (n1) != int or type(n2) != int:
        print("Only Integers Allowed")

    else:
        print(n1+n2)


addition(100,400)



def full_name(first, middle, last):


    print(
        f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")



full_name(" seraj   " , 'mohmad', "alkhraet")