the_file = None

the_comint = 5

while the_comint > 0 :

    try:

         print("Enter The File Name With Absolute Path To Open")

         print(f"You Have {the_comint} Tries Left ")

         print("Example: S:\My_Python\yourFiles.extension ")

         the_file_name_path= input("file name => :").strip()

         the_f_s= open(the_file_name_path,"r")
              
         print(the_f_s.read())

         break

    except FileNotFoundError:
       
       print("File Not Found please Be Sure The Name Is Valid")

       the_comint-=1

    except:
       
       print("Error Happen ")
       

    finally:
       
        if the_f_s is not None:
          
              the_f_s.close()

              print(" File Close.")

else:
   print("All Trise Is Done")

