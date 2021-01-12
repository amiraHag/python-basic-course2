# ------------------------------------
# ------------ Dictionary ------------
# ------------------------------------

# setdefault()

user = {
  "name": "Amira"
}
print(user)
user.setdefault("age", 3)
user.setdefault("rating")
print(user)
print("*" * 50)

# popitem()

user2 = {
  "name": "Amira"
}
print(user2)
user2.update({"age":30})
print(user2.popitem())
print(user2)
print("*" * 50)

# items()

user3 = {
  "name": "Amira",
  "skill": "Programming"
}

allItems = user3.items()
print(user3)
user3["age"] = 36

print(allItems)

print("*" * 50)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b))
