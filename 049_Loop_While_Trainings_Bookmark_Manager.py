# -----------------------------
# -- Loop => While Training  --
# -- Simple Bookmark Manager --
# ----------------------------- 

# Empty List Fill Later
myFavouriteWebs = []

# MaximumWebs Allowed Websites 
maxmimumwebs = 5

while maxmimumwebs > 0:

     # Input The New Website
     web = input("Website Name Without https:// ")

     # Add The New Website To The List 
     myFavouriteWebs.append(f"https://{web.strip().lower()}")
 
     # Decrease One Number Form Allowed Websites
     maxmimumwebs-=1 # maxmimumwebs = maxmimumwebs - 1
     # Print() The Add Message
     print(f"Website Added,{maxmimumwebs} Places Left")

     # Print The List 
     print(myFavouriteWebs)


else:
     
     print("Bookmark Is Full,You can Add More")

# Check If List Is not Empty
if len(myFavouriteWebs) > 0 :

     # Sort The List 
     myFavouriteWebs.sort()

     index = 0

     print("Printing The List Of websites in Your Bookmark")

     while index < len(myFavouriteWebs) :
            
             print(myFavouriteWebs[index])

             index +=1 # index = index + 1