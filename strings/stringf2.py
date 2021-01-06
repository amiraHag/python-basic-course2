#------------------------------------
#---------String Formatting----------
#------------------------------------


name ="Amira"
age= 30
rank=10

print("My name is: {}".format(name))

print("My name is: {}".format(name))
print("My name is: {} and My age is: {} ".format(name,age))
print("My name is: {:s} and My age is: {:d}  and My rank is: {:f}".format(name,age,rank))

#placeholder in format {}
# {:s} for String
# {:d} for number (digit)
# {:f} for float

n="Amira"
l="Python"
y=10
print("My name is {} and I Love {} Language with {:d} years experience".format(n,l,y))

#Control floating point number
# {:f}
# {:.1f}
#{:.2f} or any number of digit you want to be after the floating point
myNumber =10
print("My Number is : {:d}".format(myNumber))
print("My Number is : {:f}".format(myNumber))
print("My Number is : {:.1f}".format(myNumber))
print("My Number is : {:.2f}".format(myNumber))


# Truncate or Slice the string
# {:s}
# {:.1s}
#{:.7s} or any number of char you want to display from the string
myLongString ="Hello all we love python and have experience on it"
print("Message is : {} ".format(myLongString))
print("Message is : {:.7s} ".format(myLongString))
print("Message is : {:.12s} ".format(myLongString))


# format money
myMoney = 529741497456
print("My Money in Bank is : {:d} ".format(myMoney))
print("My Money in Bank is : {:_d} ".format(myMoney))
print("My Money in Bank is : {:,d} ".format(myMoney))
# print("My Money in Bank is : {:&d} ".format(myMoney)) Error -> ValueError: Invalid format specifier

# Re-arrange items
a, b, c ="One", "Two", "Three"
print("My Numbers are : {} {} {} ".format(a,b,c))
print("My Numbers are : {1} {2} {0} ".format(a,b,c))
print("My Numbers are : {2} {0} {1} ".format(a,b,c))

x, y, z =10,20,30
print("My Numbers are : {} {} {} ".format(x,y,z))
print("My Numbers are : {2} {1} {0} ".format(x,y,z))
print("My Numbers are : {2} {0} {1} ".format(x,y,z))
print("My Numbers are : {2:.2f} {0:d} {1:.1f} ".format(x,y,z))


#Format in ver 3.6+
# add f letter befor "" of the string allow you to write the var strait in {} without format function
myName="Amira"
myAge=30
print("My Name is {myName} and My Age is {myAge}")
print(f"My Name is {myName} and My Age is {myAge}")
