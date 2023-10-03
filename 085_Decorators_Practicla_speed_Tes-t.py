# ----------------------------------------
# -- Decroators => Practical Speed Test --
# ----------------------------------------
from time import time

# def myDecroators(func):

#    def nestedFunc(*numbers):

#        for numder in numbers :

#            if numder < 0 :

#             print("Beware One Of The Numbers Is Less Than Alkherat")

#        func(*numbers)
#    return nestedFunc

#@myDecroators
#def calculate(n1,n2,n3,n4):
#    print(n1+n2+n3+n4)


# calculate(5,100,5,14)

def speedTest (func):
    def wrapper():
        start = time()
        func()
        end = time()

        print(f"Funiction Runnuing Time Is: {end - start}")
    return wrapper

@speedTest
def bigloop():
    for number in range(1, 20000):
        print(number)

bigloop()