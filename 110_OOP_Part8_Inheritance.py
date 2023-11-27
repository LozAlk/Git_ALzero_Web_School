# -------------------------------------------------
# -- Object Ortiented Programming => Inheritance --
# -------------------------------------------------


class Food :
    def __init__(self,name,price):

        self.name = name

        self.price = price

        print(f'{self.name} Food is Created From Base Class = {self.price} ')

    def eat(self):

        print('Eat Methods From Base Class')

class Apple(Food):

    def __init__(self,name,price,amout):

        #Food.__init__(self,name)

        super().__init__(name,price)
        self.amout = amout
        print(f'{self.name} Apple is Created From Derved Class = {self.price+40} And Amount is {self.amout} ')

    def get_From(self):
        print('Get From Tree From Derived Class')


 


#food_now = Food("Pattza")
#food_now.eat()
food_tow = Apple("Food",160, 700)
food_tow.eat()
food_tow.get_From()