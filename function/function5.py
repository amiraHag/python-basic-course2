# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

def show_skills(*skills):

  print(type(skills))

  for skill in skills:

    print(f"{skill}")

show_skills("Html", "CSS", "JS")

print("*"*40)
mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%"
}

def display_skills(**skills):

  print(type(skills))

  for skill, value in skills.items():

    print(f"{skill} value is {value}")

display_skills(**mySkills)
