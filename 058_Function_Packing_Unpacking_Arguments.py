# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------


#print(1, 2, 3, 4)

#myList = [1, 2, 3, 4]

#print(myList)
#print(*myList)


#def say_hello(*peoples): # n1, n2, n3, .........

#    for name in peoples :

#        print(f"Hello {name} ")

#say_hello("Seraj", "Ahmad", "Lool","Älkherat","Soso")


def show_details(name, *skills) :
    
    print(f"Hello {name} Your Skills Is:")

    for skill in skills:

              print(skill)
       

show_details("Seraj","Html","Css","Js","Python")
