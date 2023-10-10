# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is Aruntime Error Reporting Mechanism
# [2] Exceptions Gives You The Message To Understand The Problem'
# [3] Traceback Gives You The Line To Look For The Code in This Line 
# [4] Exceptions Have Types (SyntaxError, IndexError , KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------------




#x = 10 
#if x < 0:
    
#    raise Exception(f"The Number {x} Is Less Than ALkherat")

#    print("This Will Not Print Because The Error")

#else:
#    print(f"{x} Is good Number and ok")

#print("Print Message After If Condition")


x = "Seraj"
if type (x)!= int:
    
    raise ValueError(f"The Sytring {x} Is Less Than ALkherat")


else:
    print(f"{x} Is good Number and ok")

print("Print Message After If Condition")