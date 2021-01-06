#------------------------------------
#----------String Methods------------
#------------------------------------

#split() rsplit()
#split the string to several elements in a list
#split string based on space by default
#split parameters are optional (separator , max split)
#separator is the char that the function will split based on
#the max split is the max number of elements that the string could be split into and the remaining part of string will be added to the last element
a="I Love Python Programming Language"
print(a.split())
print(type(a.split()))

b="ILovePythonProgrammingLanguage"
print(b.split())
print(type(b.split()))

c="I-Love-Python-Programming-Language"
print(c.split('-'))
print(type(c.split('-')))

d="I-Love-Python-Programming-Language"
print(d.split('-',2))

#rsplit make split from the right
e="I-Love-Python-Programming-Language"
print(e.rsplit('-',2))

#center()
# one argument mandatory ma-elements number
# second argument optional (default space) char to padd the string with
n="Amira"
print(n.center(15))
print(n.center(15,'#'))
print(n.center(25,'-'))
print(n.center(25,'@'))

#count()
# one argument mandatory => char or text you need to count in your string
# this argument case sensitive
# second argument optional start position at which you will start search
# third argument optional end position at which you will end your search the end index excluded
f="My name is Amira H M"
print(f.count("M"))
print(f.count(" "))
print(f.count("Amira"))
print(f.count("amira"))
print(f.count("a",0,15))
print(f.count("a",0,16))

# swapcase()
# change each capital letter with small letter and viseverse
h="I love code"
print(h.swapcase())

#startswith()
# one argument mandatory => char or text you need to ask if yout string start with
# this argument case sensitive
# second argument optional start position at which you will start search
# third argument optional end position at which you will end your search the end index excluded
j="The weather is fine"
print(j.startswith("T"))
print(j.startswith("t"))
print(j.startswith("w"))
print(j.startswith("w",4))
print(j.startswith("h",1,4))
print(j.startswith("The w",0,4))
print(j.startswith("The w",0,5))


#endswith()
# one argument mandatory => char or text you need to ask if yout string end with
# this argument case sensitive
# second argument optional start position at which you will start search
# third argument optional end position at which you will end your search the end index excluded
l="The weather is fine"
print(l.endswith("e"))
print(l.endswith("E"))
print(l.endswith("w"))
print(l.endswith("w",0,4))
print(l.endswith("h",0,2))
print(l.endswith("The w",0,4))
print(l.endswith("The w",0,5))
