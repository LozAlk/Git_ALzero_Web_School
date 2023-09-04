# --------------------------------------------------
# -- Function Packing Unpacking Arguments **Kwargs --
# ---------------------------------------------------


"""
def Show_skills(*skills):

    print(type(skills))

    for skill in skills:

        print(f"{skill}")


Show_skills("Html","Css","Js")
"""
myskills ={
    'HTML' :"80%",
    'Js' : "70%",
    'pYTHON': "60%",
    'Css' :"50%",
    'Go': "30"
}


def Show_skills(**skills):

    print(type(skills))

    for skill,value  in skills.items():

        print(f"{skill} => {value}")


Show_skills(**myskills)
