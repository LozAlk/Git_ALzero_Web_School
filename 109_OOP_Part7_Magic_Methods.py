# -----------------------------------------------
# -- Object Oriented Programming => magic Methods
# -----------------------------------------------
# Everything in Python Is An Object
# __init__ Called Automatically When Instantuating Class
# self.__class__ The class To Which a class instance Belongs
# __str__ Gives a Human-Redable Output of the Object
# __len__ Returns the Length of the Container
#                        Called When we Use the Built-in len() Function on the Object
# -----------------------------------------------------------------------------


class Skill:
    def __init__(self):
        self.skills = ['Html','js','Css']

    def __str__(self):
        return f'This is My Skills I Have {self.skills}'

    def __len__(self):
        return len(self.skills)





profile = Skill()
#
#print(profile)
print(len(profile))

profile.skills.append('PHP')
profile.skills.append('MySQL')
profile.skills.append("Pthon")

print(profile)
print(len(profile))
#print(profile.__class__)
        
#my_sting = 'Seraj'
#print(type(my_sting))
#print(my_sting.__class__)
#print(dir(str))

#print(str.upper(my_sting))