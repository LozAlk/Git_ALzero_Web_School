# ----------------------------------
# -- Practical Membership control --
# ----------------------------------

# List contains Admins
admins = ["Seraj","Osama","Sameh","Manal","Rahma","Mahmoud","Enas"]

# Login 
name = input(" Please Type Your Name ? ").strip().capitalize()

# If Name Is In Adimn

if name in admins :

   print(f"Hello {name} welcome Back")
  
   option = input("Delete or Update Your Name ? ").strip().capitalize()

   print(option)

    # Update Option
   if option == 'Update' or option == 'U':
      
      theNewName = input("Your New Name Please ? ").strip().capitalize()

      admins[admins.index(name)] = theNewName

      print("Name Updated.")

      print(admins)

      # Delete Option
   elif option == "Delete" or option == "D":
      
       admins.remove(name)

       print("Name Deleted")

       print(admins)


       # Wrong Option
   else:
      print("Wrong Option Choosed")

else :

  status = input("Not Aidmin, Add You Y, N ?").strip().capitalize()
  if status == "Yes" or status == "Y" :
     
     print("You Have Been Added")

     admins.append(name)
     print(admins)

  else:
     
     print("You Are Not Added ")