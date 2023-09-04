# --------------------------------------
# -- Iterable vs iterator --
# --------------------------
# Iterable 
# [1] Object Contains Date That Can Be Iterated Upon 
# [2] Examples (String, List, Set, Tuple, dictionary)
# ---------------------------------------------------
# Iterator
# [1] Object Used To Iterator Over Iterabel Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator Form Iterabel When Using iter() Method
# [3] For Loop Already Calls iter() Method on the Iterabel Behind Teh Scene
# [4] Gives "StoopIteration" If Theres No Next Element 
# -------------------------------------------------------------


myString = "Seraj"

myList = [1,2,3,4,5]

#for letter in myString:

#    print(letter,end=" ")

#for number in myList :

#    print(number,end=" ")

#myIterator = iter(myString)
#print(next(myIterator))
#print(next(myIterator))
#print(next(myIterator))
#print(next(myIterator))
#print(next(myIterator))


for letter in iter("Alkherat"):
    print(letter,end=" ")