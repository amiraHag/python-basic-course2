# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable, start=0)

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 1)

print(type(mySkillsWithCounter))

for counter, skill in mySkillsWithCounter:

  print(f"{counter} - {skill}")

print("*" * 40)

# help()

#print(help(print))

print("*" * 40)

inputText = "AmiraHM"

print(reversed(inputText))

for inputChar in reversed(inputText):

  print(inputChar)

for mySkill in reversed(mySkills):

  print(mySkill)
