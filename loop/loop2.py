# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myList = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

a = 0

while a < len(myList):
    print(f"#{str(a+1).zfill(2)} {myList[a]}")
    a += 1

else:

  print("All List Members Printed.")
