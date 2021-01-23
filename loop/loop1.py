# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

userRate = int(input("Please enter your rate:").strip())

while userRate > 5:
    print(f"The user rate is {userRate}")
    userRate-=1
else:
    print("The else condition implemented after while condition not met")
print("End of The Loop")

while False:
    print("The line will not printed")
print("Implementation after the loop")
