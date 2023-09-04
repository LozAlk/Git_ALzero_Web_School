# ------------------------
# -- Function => lambda -- 
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name 
# [2] You Can Ues It In Inline Without Definig It 
# [3] You Can Use It In Return Data From Another Function 
# [4] Lambda Used For Simple Function And Def Gandle the Large Tasks 
# [5] Lambda is One Single Expression not Block Of Code 
# [6] Lambda Type is Function
# -------------------------------------------------------------------

def say_hello (name,age) : return f"Hello {name} your Age Is: {age}"

hello = lambda name, age : f"Hello {name} Your Age Is: {age} "

print(say_hello("Seraj",22))

print(hello("Sersj",22))

print(type(hello))
