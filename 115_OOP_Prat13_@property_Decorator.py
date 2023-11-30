# ----------------------------------------------------
# Object Oriented Programing => @Property Decorator --
# ----------------------------------------------------

class Member:
    def __init__(self,name,age):

        self.name = name

        self.age = age

    def dey_hello(self):

        return f"Hello {self.name}"
    @property

    def get_str_l(self):
        
        return self.age * 365
    


one = Member("Seraj",22)

print(one.dey_hello())
print(one.name)

print(one.age)

#print(one.get_str_l())