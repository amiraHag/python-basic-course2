# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

alphaList = ["A", "B", "C", "D", "F"]

noList = [1, 2, 3, 4, 5]

for char in alphaList:

  print(f"{char} Is Element in First List. ")

  for no in noList:

    print(f" {no} in the Seocnd List")

print("*"*40)
print("*"*40)
peoples = {
  "Amira": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Sara": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Yumna": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}

for person in peoples:
    print(f"The Person Name : {person}")
    for skill in peoples[person]:
        print(f"The Person Skill : {skill} has value of {peoples[person][skill]}")
    print("*"*40)

print("*"*40)
rentValue=1200
total=0
for i in range(15):
    total += 12*rentValue
    print(f"year {i} the rent will be {rentValue}")
    rentValue+= rentValue*10/100
    print(f"{total}")
