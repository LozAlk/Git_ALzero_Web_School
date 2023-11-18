# --------------------------------------------------------------------
# -- Object Orinented Porgramming => Istance Attributes And Methods --
# --------------------------------------------------------------------
# Self : Point To Instance Cerated From Class 
# Instance  Attinbutes: Instance Attributes Defined Inside The Constructor 
# ------------------------------------------------------------------------
# Instance Methods : Task Self Parmeter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function 
# Instance Methods Can Freely Access Attributes And Methods On The same Object 
# Instance Methods Can Access The Class Itself
# -------------------------------------------------------------


class Meber:
    def __init__(self,frist_name,middle_name,list_name,agye_name):
        self.fname = frist_name
        self.mname = middle_name
        self.lname = list_name
        self.aname= agye_name

    def get_File_name(self):

        return f"{self.fname} {self.mname} {self.lname} {self.aname}"
    
    def name_Whie_title(self): 
                 
                
        if self.aname == "Seraj":

            return f"Hello Mr.{self.fname}"
        
        elif self.aname == "Loan":

            return f"Hello Miss.{self.fname}"
        
        else:

            return f"Hello {self.fname}"
    def my_name_if_valuess(self):

        return f"{self.name_Whie_title()}, Your Full Name Is: {self.fname}"

    


meber_one =   Meber   ("Seraj","Ahmad","Ail","Alkherat")
meber_two =   Meber   ("Ail","Sad","Rame","Lona")
meber_three = Meber ("Mona","Sara","Asad","Mona")


#print(meber_three.get_File_name())

#print(meber_three.name_Whie_title())


print(meber_one.my_name_if_valuess())