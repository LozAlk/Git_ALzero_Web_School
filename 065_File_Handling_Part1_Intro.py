# -------------------
# -- File Handling --
# -------------------
# "a" Append Open File For Appending Values, Create File If Not Exists
# "r" Read  [Dafault Value] Open File For Read And Give Error Ifn File Is Not Exists
# "w" write Open File Foe Writing, Create File If Not Exists
# "X" Create File, Give Error If File Exists
# ------------------------------------------

import os  

# Main Current Working Directory
#print(os.getcwd())

# Dicretory For The Opened File 
#print(os.path.dirname(os.path.abspath(__file__)))

# Change Current Working Dicretory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#print(os.getcwd())

print(os.path.abspath(__file__))

#file = open(r"S:\nFiles\seraj.txt")

#file = open("S:\Files\seraj.txt")

#print(file)
#file = open("seraj.txt")