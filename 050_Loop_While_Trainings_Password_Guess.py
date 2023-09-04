# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess  --
# ----------------------------

tries = 4

mainPassword = "Seraj@123".strip()

inputPassword = input("Write Your Password:")

while inputPassword != mainPassword : # True
     
     tries -=1 # tries = tries - 1

     print(f"Wrong Password, {'List'if tries == 0 else tries} Chance Left")

     inputPassword =input("Write Your Password:")

     if tries == 0:
  
             print("All Tries Is Finished.")

             break 
     
             print("will Not Print")

else:
          print("Correct Password ")