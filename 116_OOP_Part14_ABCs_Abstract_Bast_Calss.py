# ---------------------------------------------------------------
# -- Objcet Oriented Porgramming => ABCs => Abstract Bast Class
# ---------------------------------------------------------------
# - Class Called Abstract Class if Has One Or More Abstract Methods  
# - abc Module in Python Provides Infrastructure for Defining Custom Abstract Base Classes. 
# -By Adding @absttractmethod Decorator On The Methods
# -ABCMeta Class In a Metaclass Used For Defining Abstract Base Class
# ---------------------------------------------------------------------


from abc import ABCMeta , abstractmethod


class Programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass

    def has_abstract(self): 
        pass

class Python(Programming):

    def has_oop(self):

        return "Yes"
    

class Pascal(Programming):

    def has_oop(self):

        return "No"
    


one = Pascal()

print(one.has_oop())