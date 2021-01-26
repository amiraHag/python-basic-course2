# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

print(1, 2, 3, 4)

myList = [1, 2, 3, 5]

print(myList)
print(*myList)
print("*"*40)

def say_hello(*names):
    for name in names:
        print(f"Hello {name}")

say_hello("Amira", "Sara", "Ahmed", "Suka")
print("*"*40)

def display_tasks(name, *skills):
    print(f"Hello {name}, your skills are:")
    for skill in skills:
        print(f" - {skill}")
display_tasks("Amira", "Python", "PHP", "JAVA", "Ruby")
print("*"*40)
