# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------


passTries = 4

correctPassword = "ABC@123"

inputPassword = input("PLease Enter Your Password: ")

while inputPassword != correctPassword:

  passTries -= 1

  print(f"Wrong Password, { 'Last' if passTries == 0 else passTries } Chance Left")

  inputPassword = input("Write Your Password: ")

  if passTries == 0:

    print("All Password Tries Is Finished.")

    break

    print("Will Not Print")

else:

  print("Correct Password, Welcome Back")
