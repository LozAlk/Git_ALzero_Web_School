# -------------------------
# -- Decoeators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming 
# [2] Everything in python is Object Even Function
# [3] Decoeators Take A Function and Add Some Functionality and Return It 
# [4] Decoeators Wrap Other Function and Enhance Their Behaviour
# [5] Decoeators is Higher Order Function (Function Accept Function As Parameter)
# -------------------------------------------------------------------------------

def myDecorator(func):

    def nestedfunc():

        print("Before")

        func()

        print("After")


    return nestedfunc
@myDecorator
def sayhello():

    print("Hello Form Say Hello Function")


@myDecorator
def sayHoeareyou():

    print("Hello Form Say Hello Function")



sayhello()

print(" Hello ".center(40,"#") )

sayHoeareyou()
    
