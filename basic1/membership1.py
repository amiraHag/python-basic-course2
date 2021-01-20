# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String

name = "Amira"
print("r" in name)
print("a" in name)
print("S" in name)

print("*" * 50)


# List

girls = ["Sara", "Amira", "Suka"]
print("Sara" in girls)
print("sara" in girls)
print("Ahmed" in girls)
print("Marwa" not in girls)

print("*" * 50)


# Using In and Not In With Condition

availableCountries = ["EGYPT", "KSA", "UAE"]
availableCountriesDicount = 30

availableCountries2 = ["ITALY", "USA"]
availableCountries2Discount = 10

userCountry = input("Please enter your country:").strip().upper()

if userCountry in availableCountries:

  print(f"Hello You Have A Discount Equal To ${availableCountriesDicount}")

elif userCountry in availableCountries2:

  print(f"Hello You Have A Discount Equal To ${availableCountries2Discount}")

else:

  print("You Have No Discount")
