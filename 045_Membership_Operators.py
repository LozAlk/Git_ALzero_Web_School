# --------------------------
# -- Membership Operators --
# --------------------------
# in 
# not in
# --------------------------


# String 

name = "seraj"
print("s" in name)
print("e" in name )
print("S" in name )
print("E" in name )

print("#"*40)

# List 
friends =["seraj","abood", "lies"]
print("seraj" in friends)
print("lies" in friends)
print("abood" not in friends)

print("#"*40)

# Using In and Not In with Condition

ContinuesOne = ["Egypt","KSA","Kuwait", "Bahrain","Syria"]
ContinuesOneDiscount = 80


continuesTwo = ["Italy","Usa"]
continuesTwoDiscount = 50

myCountry = (input( " Your are from center ? ").strip().capitalize())

if myCountry in ContinuesOne:
    print(f"Hello You Have A Discount Equal To $ {ContinuesOneDiscount}")

elif myCountry in continuesTwo:
    print(f"Hello you Have A Discount Equal To $ {continuesTwoDiscount}")


else:
    print("You Have No Discount")  