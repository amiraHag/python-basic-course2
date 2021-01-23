# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

myRates = {
"First Year": 75,
"Second Year": 80,
"Third Year": 82.5,
"Fourth Year": 92.2,
"Fifth Year": 91.2
}

print(myRates.items())
print("*"* 40)

for rate in myRates:
    print(f"The Rate for {rate} is {myRates[rate]}")
print("*"* 40)

for rate, rateValue in myRates.items():
    print(f"The Rate for {rate} is {rateValue}")
print("*"* 40)

mySkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}

for main_key, main_value in mySkills.items():

  print(f"{main_key} Progress Is: ")

  for child_key, child_value in main_value.items():

    print(f"- {child_key} => {child_value}")
