#------------------------------------
#----------String Methods------------
#------------------------------------

# index(substring, start, end)

a= "I Love Python"
print(a.index("L"))
print(a.index("L", 0,5))
# print(a.index("L", 3,10))    # Error :  ValueError: substring not found


# find(substring, start, end)

b= "I Love Python"
print(b.find("L"))
print(b.find("L", 0,5))
print(b.find("L", 3,10)) # -1  :  substring not found


# rjust(Width, Fill Char)           ljust(Width, Fill Char)

c = "Hello"
print(c.rjust(10))  # right justified put space before the text to make the string right justified
print(c.rjust(10,"#"))
print(c.ljust(10))  # left justified put space after the text to make the string left justified
print(c.ljust(10,"#"))

# splitlines() -> return list at which each line is separate element
d="""First Line
Second Line
Third Line"""
print(d)
print(d.splitlines())

e= "First Line \nSecond Line \nThird Line"
print(e)
print(e.splitlines())

# expandtabs() specify no of space in each tab in the string
f= "I\tLove\tPython"
print(f)
print(f.expandtabs(2))
print(f.expandtabs(20))


one="I Love Python And 3G"
two="I Love Python And 3g"
three=" "
four=""
five="i love python"
six="I Love Python"
seven="I LOVE PYTHON"

print(one.istitle())
print(two.istitle())
print(three.isspace())
print(four.isspace())
print(five.islower())
print(six.islower())
print(five.isupper())
print(seven.isupper())

eight="amira_m"
nine="amira99"
ten="amira--m"
print(eight.isidentifier())
print(nine.isidentifier())
print(ten.isidentifier())

x="AaaaBaaaa"
y="AaaaBaaaa65"
print(x.isalpha())
print(y.isalpha())

print(x.isalnum())
print(y.isalnum())
