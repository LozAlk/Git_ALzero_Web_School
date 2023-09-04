# --------------------------------------------------
# -- Calculate Age Advanced Version and Training -- 
# --------------------------------------------------

# Write A Very Beautiful Note
print(80*"#")
print(" You Can write The First Letter Or Full The Tiem Unit ".center(80,'#'))
print(80*"#")
# Collect age Data 

age = (input(" Please Write Your Age ?")).strip()

# Collect Tiem Unit Data
uint = (input(" Please Choose Tiem Unit: [Months], [Weeks], [Days].?")).strip().lower()

# Get Tiem Uints

months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if uint == 'months' or uint  == 'm':
    print("You Choosed The Uint Months")
    print(f"You Lived For {months:,} Months. ")

elif uint == 'weeks' or uint == 'w':
    print("You Choosed The Uint Weeks")
    print(f"You Lived For {weeks:,} Weeks. ")

elif uint == 'Days' or uint == 'd':
    print("You Choosed The Uint Days")
    print(f"You Lived For {days:,} Days. ")

print('#'*80)
print(' Oky Dank je Veel '.center(80,'#'))
print('#'*80)