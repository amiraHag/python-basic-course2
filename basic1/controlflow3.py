# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

userCountry = input("Where are you from?").strip().capitalize()

if userCountry == "Egypt" : print(f"The Weather in {userCountry} Is 5")
elif userCountry == "Ksa" : print(f"The Weather in {userCountry} Is 22")
else : print("Country is Not in The List")

# Short If (Ternary)
# Condition If True | If Condition | Else | Condition If False
userRate = int(input("What is your rate?").strip())
print(f"Rate: {userRate}, Keep the Good Work." if userRate > 6 else f"Rate: {userRate}, You should do better")
