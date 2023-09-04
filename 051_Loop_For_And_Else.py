# -----------------
# -- Loop => For --
# -----------------
# For item in iterable_object :
# Do Something with Item
# -----------------------------
# item Is A Vairable You Create And Call Whenever You Want 
# item refer to the Current Position and will run and visit all items to the end
# iterabl_object => Sequence [list, tuple, set, dict, string of chercaters, etc ...]
# -----------------------------------------------------------------------------------



myNumbers = [1,2,3,4,5,6,7,8,9]

for numbers in myNumbers :
    # print(numbers * 17)

    if numbers % 2 == 0 : # Even
        print(f"The Numbers {numbers} Is Even.")


    else :
        print(f"The Numbers {numbers} Is Odd.")

else :

   print("The Loop Is Finished")


myName = "Seraj"

for letter in myName :

    print(f"[ {letter.capitalize()} ] ")