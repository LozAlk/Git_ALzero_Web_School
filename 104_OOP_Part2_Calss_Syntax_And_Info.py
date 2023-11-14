# ---------------------------------------------------------
# -- Object Oriented Programming =>Calss Syntax And Info --
# [01] Class is The Blueorint Or Construtor Of The Object 
# [02] Class Instantuate Means Create Instance of A Class
# [03] Instance => Object Created From Class And Have Thier Methods And Attributes 
# [04] Class Defined With Keyword Class 
# [05] Class Name Written With PascalCase [UpperCameCase] Style
# [06] Class May Contains Methods And Attributes 
# [07] When creating Object Python Look For The Built In __init__Method
# [08] __init__Method Called Every Tiem You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object 
# [10] Any Method With Two Underscore in Tne Start And End Callled Dunder or Magic Method 
# [11] Self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] Self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object 
# -----------------------------------------------------------------------------------------


# Syntax 
# Class Name :
#            Constructor => Do Instantiation [Create Instance From A Class]
#            Each Instane Is Separate Object 
#             def __init__ (self,other_data)
#                        Body of Function 
class Member:
    def __init__(self):
        print("A New Meber Has Been Added ")


member_Onw  = Member()
member_Tow  = Member()
member_Thre = Member()

print(member_Onw.__class__)


my_Dictionary = {
    'name': 'Seraj',

    'Age': 23 ,

    'Monthly_salary': 5000 ,

    'Yearly_salary' : ' ' # Something 
}
