# -----------------------------------------------------------------
# -- Object oriented Programming => Instance Attributes and Methods
# -----------------------------------------------------------------
# Self:Point To Instance Created From Class 
# Instance Attribrutes: instance Attributes Defined Inside The Constructor
# ------------------------------------------------------------------------
# Instace Methods: Take Self Parmaeter Which Point To Instace created From Class
# Instace Methods Can Have More Than One Parameter Like Any Function
# Instace Methods Can Freely Access Attribrutes And Methods On The Same Object
# Instace Methods Can Access The Class Itself
# -------------------------------------------------------------
class Mabaer:
    def __init__(self, first_name, modil_name, last_name):

        self.fname= first_name
        self.mname=modil_name
        self.lname=last_name


mabaer_one = [Mabaer("Seraj","mahmood","Ail")]

mabaer_two = [Mabaer("Lolo","Gamil","loop")]

mabaer_tree = [Mabaer ("Gad","Oagd","Braa")]

print(mabaer_one[0].fname, mabaer_one[0].mname, mabaer_one[0].lname)
print(mabaer_two[0].fname)
print(mabaer_tree[0].lname)

