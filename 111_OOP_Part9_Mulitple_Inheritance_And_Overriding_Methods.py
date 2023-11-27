# --------------------------------------------------------
# -- Object Oriented Progamming => Multiple Inheritance --
# --------------------------------------------------------

class BasOne:
    def __init__(self) :
       
       print('Base One')

    def func_one(self) :
       
       print('One'.upper())

class BasToe:
   
   def __init__(self) :
      
      print('Base Two')

   def func_two(self) :
       
       print('Two'.upper())

class Derived(BasOne,BasToe):
   pass 


my_var = Derived()
print(my_var.func_one)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()



#print(Derived.mor())