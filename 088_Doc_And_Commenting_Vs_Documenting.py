# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documenting String For Class, Module or Function 
# [2] Can Be Accessed From The Help and Doc Attributss
# [3] Mede For Understanding The Functionality of the Complex Code 
# [4] Theres One Line And Multiple Line Doc String
# -----------------------------------------------------------------


print(" Doc String & Commenting vs Documenting ".center(80,"#"))

def alkherat(name):
    '''Alkherat Function
    It Say Hello From kherat
    Parmeter:
    name => Person Name That Use Function
    Return:
    Return Hello Message To The Preson'''
    print(f"Hello {name} From Kherat")

print(alkherat.__doc__)
#alkherat("Serag")
#help(alkherat)
#print(dir(alkherat))

print(" & Klaar & ".center(80,"#"))