#------------------------------------
#---------String Formatting----------
#------------------------------------

name ="Amira"
age= 30
rank=10

print("My name is: "+name)
# print("My name is: "+name +" My Age is: " + age) -> TypeError: must be str, not int


# %s placeholder for string %d placeholder for digit %f placeholder for float
print("My name is: %s" % name)
print("My name is: %s and My age is: %d " % (name,age))
print("My name is: %s and My age is: %d  and My rank is: %f" % (name,age,rank))

#placeholder
# %s for String
# %d for number (digit)
# %f for float

n="Amira"
l="Python"
y=10
print("My name is %s and I Love %s Language with %d years experience" %(n,l,y))

#Control floating point number
# %f
# %.1f
#%.2f or any number of digit you want to be after the floating point
myNumber =10
print("My Number is : %d" % myNumber)
print("My Number is : %f" % myNumber)
print("My Number is : %.1f" % myNumber)
print("My Number is : %.2f" % myNumber)


# Truncate or Slice the string
# %s
# %.1s
#%.7s or any number of char you want to display from the string
myLongString ="Hello all we love python and have experience on it"
print("Message is : %s " % myLongString)
print("Message is : %.7s " % myLongString)
print("Message is : %.12s " % myLongString)
