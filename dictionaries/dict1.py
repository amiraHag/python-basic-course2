# ------------------------------------------------------------------------------
#
# ------------------------------------
# ------------ Dictionary ------------
# ------------------------------------
#
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ------------------------------------------------------------------------------

# Dictionary

user = {
  "name": "Amira",
  "age": 30,
  "country": "Egypt",
  "city":"Cairo",
  "language":["Python","Java","PHP","Ruby"],
  1:"value for integer key",
  (1,"A",True):"Value for tuple key"
}
print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())
print("*"*40)

# Two-Dimensional Dictionary

languages = {
  "First": {
    "name": "Html",
    "progress": "80%"
  },
  "Second": {
    "name": "Css",
    "progress": "90%"
  },
  "Third": {
    "name": "Js",
    "progress": "90%"
  }
}

print(languages)
print(languages['First'])
print(languages['Third']['name'])
print("*"*40)

# len() method return the length of the dictionary
print(len(languages))
print(len(languages['Third']))
print("*"*40)


# Create Dictionary From Variables

dict1 = {
  "name": "Dictionary 1",
  "rating": 8
}

dict2 = {
   "name": "Dictionary 2",
   "rating": 8.5
}

dict3 = {
    "name": "Dictionary 3",
    "rating": 9.4
}

allDict = {
  "First": dict1,
  "Second": dict2,
  "Third": dict3
}

print(allDict)
