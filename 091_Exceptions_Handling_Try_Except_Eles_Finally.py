# --------------------------------
# --    Excwptions Handling    --
# -- Try |Except |Else|Finally --
# --------------------------------
# Try      => Test The Code For Errors 
# Except   => Handle The Errors
# -----------------------------
# Else     => If No Errors
# Finally  => Run The Code
# --------------------------------------

print(" Try|Except |Else|Finally ".center(40,"#"))


# try:   # Try The Code And Test Errors
#    Number =(int(input("Wirt Your Age:")))
#    print("Good, This is Integer Form Try")

# except:  # Handle The Errors Its Found 
#    print("Bas, This is Not  Intger")

#else:  #  If There Its No Errors
#    print("Good, This is Integer Form Eles")

# finally:
#    print("Print Form Finally Whtaever Happens")



try:
    print(10/0)
    #print(x)
    print(int("Hello"))


except ZeroDivisionError:
    print("Cant Divide")

except ValueError:
    print("Value Error Alkherat")

except NameError:
    print("Idantifier Not Found")

except :
    print("Cant Except")
