# ------------------------------------
# --------- Boolean Operators --------
# ------------------------------------
# and
# or
# not
# -----------------------

age = 30
country = "Egypt"
rating = 10

print(age > 16 and country == "Egypt" and rating > 0)  # True
print(age > 16 and country == "UAE" and rating > 0)  # False

print(age > 40 or country == "UAE" or rating > 20)  # False
print(age > 40 or country == "Egypt" or rating > 20)  # True

print(age > 16)  # True
print(not age > 16)  # Not True = False
