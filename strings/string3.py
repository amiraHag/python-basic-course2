#------------------------------------
#----------String Methods------------
#------------------------------------

# Len(Object) return Number of elements in this Object
# Len() Built in function return Number of element in the container given to it as parameter

a= "Hello World"
b= "    Hello     World    "
print(len(a))
print(len(b))


#strip() remove spaces from left and right
#lstrip() remove spaces from left
#rstrip() remove spaces from right
a_strip="     I love Code     "
print(a_strip.strip())
print(a_strip.rstrip())
print(a_strip.lstrip())

#If char is given to strip , lstrip, rstrip it will remove the char not the space
a_strip="####I love Code####"
print(a_strip.strip())
print(a_strip.rstrip())
print(a_strip.lstrip())
print(a_strip.strip('#'))
print(a_strip.rstrip('#'))
print(a_strip.lstrip('#'))

#If more than one char we can write them all
a_strip="@#@#@#@#I love Code@#@#@#@#"
print(a_strip.strip('@#'))
print(a_strip.rstrip('@#'))
print(a_strip.lstrip('@#'))

#title() make the string title => the first char from every word capital and the char after number capital
b="i love 2d graphics and 3d graphics"
print(b.title())

#capitalize() make the first char of the first word capital
c="i love 2d graphics and 3d graphics"
print(c.capitalize())

#zfill() or zero fill take width and padd the string with zeros if the string length less than the width
d,e,f ="1","11","111"
print(d.zfill(3))
print(e.zfill(3))
print(f.zfill(3))

#upper() convert string letters to uppercase letters
g="My String"
print(g.upper())

#lower() convert string letters to lowercase letters
print(g.lower())
