# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sud --
# ----------------------------------------------------
# Split (Pattern, String, MaxSplit) => Return A List Of Elements Splitted On Each Mathch 
# Sud (Pattern, Replace, String ReplaceCount ) => Replace Matches With What You Want 
# --------------------------------------------------------------------------------------

import re

string_Onw = "I Love Python Programming Language"

seatrch_Onw = re.split(r"\s",string_Onw,1)

print(seatrch_Onw)

print("#"*40)


string_Two =  'How-To_Write_A_Very-Good-Artcle'
seatrch_Toe = re.split(r"-|_",string_Two)
print(seatrch_Toe)

print("#"*40)


for counter,word in enumerate(seatrch_Toe,1):

    if len(word)==1:
    
        continue

    print(f"Word Number:{counter} => {word.lower()}")


print("#"*40)

my_string = "I love Python "
print(re.sub(r'\s','-',my_string,1))
