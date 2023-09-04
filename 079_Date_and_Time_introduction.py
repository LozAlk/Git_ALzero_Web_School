import datetime

#print(dir(datetime))
#print(datetime.datetime)

# print The Current Date and Time
print(datetime.datetime.now())

print("#"*50)

# print The Current Year
print(datetime.datetime.now().year)

# print The Current Month
print(datetime.datetime.now().month)

# print The Current Day
print(datetime.datetime.now().day)

print("#"*50)

# Print Start and end of date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#"*50)
#print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())

print("#"*50)

# print The Current Time Hour
print(datetime.datetime.now().time().hour)

# print The Current Time Minute
print(datetime.datetime.now().time().minute)

# print The Current Time Second
print(datetime.datetime.now().time().second)

print("#"*50)

# Print Start and end To of Time 
print(datetime.time.min)
print(datetime.time.max)

print("#"*50)


# Print Specific Date
print(datetime.datetime(2001,1,15))
print(datetime.datetime(2001,1,15,1,45,55,157846))

myBirthDay = datetime.datetime(2001,1,15)
dateNow = datetime.datetime.now()

print("#"*50)

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")

print("#"*50)

print(f"I Lived For {dateNow - myBirthDay}")