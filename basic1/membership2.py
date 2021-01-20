# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
adminNames = ["Amira", "Sara", "Suka", "Ahmed", "Lola", "Lolh", "Amora"]

# Login
userName = input("Please Type Your Name ").strip().capitalize()

# If Name is In Admin
if userName in adminNames:

  print(f"Hello {userName} Welcome to our portal")

  option = input("Delete Or Update Your Name ?").strip().capitalize()

  # Update Option
  if option == 'Update' or option == 'U':

    theNewName = input("Enter Your New Name Please ").strip().capitalize()

    adminNames[adminNames.index(userName)] = theNewName

    print("Your Name Updated.")

    print(adminNames)

  # Delete Option
  elif option == 'Delete' or option == 'D':

    adminNames.remove(name)

    print("Your Name Deleted from Admins")

    print(admins)

  # Wrong Option
  else:

    print("Wrong Option Choosed")

else:

  status = input("Not Admin, Add You Y, N ? ").strip().capitalize()

  if status == "Yes" or status == "Y":

    print("You Have Been Added")

    adminNames.append(userName)

    print(adminNames)

  else:

    print("You Are Not Added.")
