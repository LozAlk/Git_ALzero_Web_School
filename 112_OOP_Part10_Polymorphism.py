# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------
class A:
    def do_somthing(self):

        print("From Class A")

        raise NotImplementedError ('Derived Class Must Implement This Method')

class B(A):
    def do_somthing(self):
        print("From Class B")



class C(A):
    def do_somthing(self):
        print("From Class C")



my_File = C()
my_File.do_somthing()
