# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

mySkills = {
    "HTML" : "80%",
    "CSS" : "90%",
    "JS" : "70%",
    "PHP" : "80%"
}

#print(mySkills.items())

#for skill in mySkills:

#    print(f"{skill}=>{mySkills[skill]}") 



#for skill_key , skill_porgress in mySkills.items():
#    print(f"{skill_key} => {skill_porgress }")



myUltimateSkills = {
    "HTML" : {
        "Main" : "80%",
        "Pugjs" : "80%"
    },
    "Css" : {
        "Main" : "90%",
        "Sass" : "80%"
    }
}

for main_key, main_value in myUltimateSkills.items():

    print(f"{main_key} Porgress Is :")

    for chid_key,chid_value in main_value.items():

        print(f"- {chid_key}=>{chid_value}")