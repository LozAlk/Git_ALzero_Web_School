# ------------------------
# -- Function Recursion --
#-------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to first Understand Recursion --
# ---------------------------------------------------------------------

# Test Word [WWWoooorrldd] # Print(x[1:])

def cleanword(word):
    
    if len(word) == 1:
        
        print(f"Print Start Function {word}")

        return word 
    
    if word[0] ==word[1]: # WWWoooorrrldd

      print(f"Print Before Return {word}")
    
      return cleanword(word[1:])
    
    print(f"Print Before Return {word}")

    return word[0]+ cleanword(word[1:])

#Stash[]

print(cleanword("WWWoooorrdd"))