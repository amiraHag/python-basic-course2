# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------

for number in range(10):
  print(number)


mySkills = {
  "Html": 9,
  "Css": 8,
  "PHP": 7,
  "JS": 9,
  "Python": 9,
  "MySQL": 9
}

print(mySkills['JS'])
print(mySkills.get("Python"))

for skill in mySkills:
  print(f"My Rate in Language {skill} Is: {mySkills.get(skill)}")
  print(f"My Rate in Language {skill} Is: {mySkills[skill]:.2f}")
