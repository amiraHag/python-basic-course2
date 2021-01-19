# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

userName = input("What\'s your Name").strip().capitalize()
userCountry = input("What\'s your Country").strip().capitalize()
userRate = int(input("What is the discount rate?").strip())

if userCountry=="Egypt" or userCountry == 'EGY':
    print(f"Hello {userName}, you are from {userCountry}")
    if userRate > 6:
        print(f"Your rate is {userRate} which is Good Keep Good Work. ")
    else:
        print(f"Your rate is {userRate} which is Not Good, You should do better. ")
elif userCountry=="KSA" or userCountry =='Saudi':
    print(f"Hello {userName}, you are from {userCountry}")
    if userRate > 6:
        print(f"Your rate is {userRate} which is Good Keep Good Work. ")
    else:
        print(f"Your rate is {userRate} which is Not Good, You should do better. ")
else:
    print(f"Hello {userName}, you are from {userCountry}")
    if userRate > 6:
        print(f"Your rate is {userRate} which is Good Keep Good Work. ")
    else:
        print(f"Your rate is {userRate} which is Not Good, You should do better. ")
