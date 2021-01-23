# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------
myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for myNumber in myNumbers:
  if myNumber % 2 == 0:

    print(f"The Number {myNumber} Is Even.")

  else:

    print(f"The Number {myNumber} Is Odd.")

else:

  print("The Loop Is Finished")

print("*" * 50)

myName = "Amira"

for letter in myName:

  print(f" [ {letter.upper()} ] ")
