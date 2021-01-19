# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

myName = "Amira"
myCountry = "Egypt"
courseName = "Python Course"
coursePrice = 100
courseDiscount_egy = 28.05
courseDiscount_ksa = 20.0

# print name and country only if i'm from Egypt
if myCountry == "Egypt":
    print(f"Hello {myName}, You are from {myCountry} ({myCountry.upper():.3s})")
    if courseDiscount_egy > 0:
        print(f"""You registered in course: {courseName}
The course cost {coursePrice} and after discount cost {coursePrice-courseDiscount_egy:.2f} """)
elif myCountry == "KSA":
    print(f"Hello {myName}, You are from {myCountry} ({myCountry.upper():.3s})")
    if courseDiscount_ksa > 0:
        print(f"""You registered in course: {courseName}
The course cost {coursePrice} and after discount cost {coursePrice-courseDiscount_ksa:.2f} """)
else:
    print(f"Hello {myName}, You are from {myCountry} ({myCountry.upper():.3s})")
    print(f"You registered in course: {courseName} and The course cost {coursePrice} ")
