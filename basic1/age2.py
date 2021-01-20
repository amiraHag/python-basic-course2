# -------------------------------------
# -- Practical Your Age with If cond --
# -------------------------------------

# Input Age
age = int(input('What\'s Your Age ? '.center(80,'*')).strip())
unit = input("Please enter the age unit you want to display your age with").strip().capitalize()

# convert age to the time parts
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('Hello You Lived For:')
if unit == "Month" or unit =="Months":
    print(f"{months} Months.")
elif unit == "Week" or unit =="Weeks":
    print(f"{weeks:,} Weeks.")
elif unit == "Day" or unit =="Days":
    print(f"{days:,} Days.")
elif unit == "Hour" or unit =="Hours":
    print(f"{hours:,} Hours.")
elif unit == "Minute" or unit =="Minutes":
    print(f"{minutes:,} Minutes.")
elif unit == "Second" or unit =="Seconds":
    print(f"{seconds:,} Seconds.")
