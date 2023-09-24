# --------------------------------------------
# -- Decorators => Function with parameters --
# --------------------------------------------

def myDecorators(func): # Decorators

    def nestedFunc(num1,num2): # Any name Its Just For Decorators

        if num1 < 0 or num2 < 0: # 

            print("Bewaer One Of The Numbers Is Less Thaa kherat")

        func(num1, num2) # Execute Function 

    return nestedFunc # Return All Data

def myDecoratorsTow(func): # Decorators

    def nestedFunc(num1,num2):# Any name Its Just For Decorators
         
        print("coming From Decorators Tow")

        func(num1, num2) # Execute Function 

    return nestedFunc # Return All Da

@myDecorators
@myDecoratorsTow
def calcukate(n1,n2):

    print(n1+n2)

calcukate(-5,90)