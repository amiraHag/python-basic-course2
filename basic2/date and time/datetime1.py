# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

print(dir(datetime))
print("*" * 40)

print(dir(datetime.datetime))
print("*" * 40)

# Print The Current Date and Time
print(datetime.datetime.now())
# Print The Current Year
print(datetime.datetime.now().year)
# Print The Current Month
print(datetime.datetime.now().month)
# Print The Current Day
print(datetime.datetime.now().day)
# Print The Current Hour
print(datetime.datetime.now().hour)
# Print The Current Minute
print(datetime.datetime.now().minute)
# Print The Current Second
print(datetime.datetime.now().second)
print("*" * 40)

# Print Start and End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("*" * 40)

print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())
# Print The Current Time Hour
print(datetime.datetime.now().time().hour)
# Print The Current Time Minute
print(datetime.datetime.now().time().minute)
# Print The Current Time Second
print(datetime.datetime.now().time().second)

print("*" * 40)

# Print Start and End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("*" * 40)

# Print Specific Date
print(datetime.datetime(1990, 3, 10))
print(datetime.datetime(1990, 3, 10, 10, 45, 55, 150364))

print("*" * 40)

myBirthDay = datetime.datetime(1990, 3, 10)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")

print(f" I Lived For {dateNow - myBirthDay}")
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")
