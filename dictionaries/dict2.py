# ------------------------------------
# ------------ Dictionary ------------
# ------------------------------------

# clear()

users = {
  "name1": "Amira",
  "name2":"Sara"
}
print(users)
users.clear()
print(users)
print("*"*40)

# update()

user = {
  "Name": "Amira",
  "Age": 10,
  "Job":"Software Developer"
}
print(user)
user["Age"] = 30
print(user)
user.update({"Country": "Egypt"})
print(user)
print("*"*40)

# copy()

a = {
  "name": "Amira"
}

b = a.copy()
print(b)
a.update({"skills": "Reading"})
print(a)
print(b)

# keys() + values()

print(a.keys())
print(a.values())
