
# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes : Attributes Defined Outside The Constrctor
# -------------------------------------------------------------


class Member:
    # Class Attribute : List of names not allowed
    not_allowed_names = ['Seraj','Shit','Baloot']
    
    # Class Attribute : Counter for the number of users
    user_num =0 

    # Constructor : Initializes the attributes of the object
    def __init__(self,frist_name,middle_name,last_naem,gender):
        self.frist_name = frist_name
        self.middle_name = middle_name
        self.last_naem = last_naem
        self.gender = gender
        Member.user_num +=1

    # Method : Returns the full name of the member
    def full_name(self):
        if self.frist_name in Member.not_allowed_names:
            raise ValueError("Name Not Allowed")
        else:
            return f"{self.frist_name} {self.middle_name} {self.last_naem}"

    # Method : Returns the full name of the member with a title
    def name_With_titl(self):
        if self.gender == "Male":
            return f"Hello Mr {self.frist_name}"
        elif self.gender == "Female":
            return f"Hello Mrs {self.frist_name}"
        else:
            return f"Hello {self.frist_name}"

    # Method : Returns all the information about the member
    def get_all_info(self):
        return f"{self.frist_name} , Your Full Name is :{self.full_name()}"
    def Delete_ueser(self):
        Member.user_num -=1
        return f'User {self.frist_name} Deleted.'

# Testing the code
print(Member.user_num)
member_one = Member ("Seraj","Mohamed","Alkaret",'Male')
member_tow = Member("Ahmad","Ali","Mahamad",'Male')
member_tree = Member("Seraj","Mohamed","Elsayed",'Female')
member_furr = Member('Shit','Hell', 'Metal','DD')


print(member_furr.Delete_ueser())
print(Member.user_num)
# Uncomment the following lines to test the methods
#print(member_one.frist_name,member_tow.middle_name,member_tree.last_naem)
#print(member_tow.frist_name)
#print(member_tree.frist_name)
#print(member_tow.full_name())
#print(member_tow.name_With_titl())
#print(member_one.get_all_info())
#
#This code demonstrates the use of class attributes in Python. The class `Member` has two class attributes: `not_allowed_names` and `user_num`. The `not_allowed_names` attribute is a list of names that are not allowed for a member. The `user_num` attribute is a counter for the number of users. The `Member` class also has a constructor (`__init__`) and three methods: `full_name`, `name_With_titl`, and `get_all_info`..</s>