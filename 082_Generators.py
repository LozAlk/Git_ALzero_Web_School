# -----------------------
# -- Generators --
# -----------------
# [1] Generators is a Function With "yield" keyword Instead of ""reaturn"
# [2] It Support Iteration and Return Generators Iterator By Calling "yield"
# [3] Generators Function Can one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not Form Begining 
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# ------------------------------------------------------------------------------


def myGenerators():


    yield 1
    yield 2
    yield 3
    yield 4


#print(myGenerators())

myGen = myGenerators()

print(next(myGen))

print("Hello From Python")

print(next(myGen))

print("Hello From Python")

print(next(myGen))

print("Hello From Python")

print(next(myGen))

print("#"*50)

for myNumber in myGen :
    print(myNumber)