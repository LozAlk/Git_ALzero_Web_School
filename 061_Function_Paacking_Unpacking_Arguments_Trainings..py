# ----------------------------------------------------
# -- Function Packing Unpacking Arguments Trainings --
# ----------------------------------------------------

myTuple = ("Html","Css","Js")

mySkills ={
    'Go':'90%',
    'Python' : '100%',
    'MySQL' : '70'
}

def show_Skills (name,*skills,**skllisswithProgres):

    print(f"Hello {name} \nSkills Without Progress Is :")

    for sklli in skills:

        print(f"- {sklli}")

        print("Skllis With Progress Is:")

        for sklli_Kye, sklli_value in skllisswithProgres.items():

            print(f"- {sklli_Kye} => {sklli_value}")

show_Skills("Seraj",*myTuple,**mySkills)