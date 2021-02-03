# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------

myAge = int(input("Please write your age:").strip())
print(myAge)
print(type(myAge))

try:  # Try The Code and Test Errors

  number = int(input("PLease Write Your Age: "))

  print("Thank You")

except:  # Handle The Errors If Its Found

  print("Sorry but This is Not an Age")

else:  # If Theres No Errors

  print("That is great, You wrote your age")

finally:

  print("Thank you and GoodLuck")



# Another Example
try:
    #print(2/0)
    #print(f"{amira}")
    print(int("Hello"))


except ZeroDivisionError:

  print("Cant Divide")

except NameError:

  print("Identifier Not Found")

except ValueError:

  print("Value Error Hello")

except:

  print("Error Happens")
