# -----------------------------------------------
# -- Object Oriented Promgramming => Encapulation
# -----------------------------------------------
# Encapsulation 
# -Restrict Access To the Data Stored In Attirbutes And Methods 
# Pubilc
# - Every Attribute And Method That We Uesd So Far Is Pubilc
# - Attributes And Methods Can Be Modified And Run From Everywhere 
# Insied Our Outside The Class
# Protected 
# - Attributes And Methods Can Be Accessed From Within The Class And Sub Classees 
# - Attributes And Methods Prefixed With One Undercore _
# Private 
# - Attributes And Methods Can Be Accessed From Winthin The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes And Methods Prefixed With Tow Underscores __
# --------------------------------------------------------------------

# --------------------------------------
# - Attributes = Variables = Properties 
# --------------------------------------
#class Member:
#    def __init__(self,name):
#        self.name = name   # Protected
      


#one = Member('Seraj')

#print(one.name)

#one.name='LOLO'

##print(one.name)



class Member:
    def __init__(self,name):
        self.__name= name   # Private
        

    
    def sey_hello(self):
        return f'Hello {self.__name}'
        

one = Member('Seraj')
# print(one.__name)
print(one.sey_hello())
print(one._Member__name)
