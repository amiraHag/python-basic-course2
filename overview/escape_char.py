#----------------------------------
# Escape Sequences Characters
# \b => back space
# \newline => Escape New line + backslash \
# \\ => Escape back slash
# \' => Escape single quote
# \" => Escape double quote
# \n => line feed
# \r => Carriage Return
# \t => horizontal tab
# \xhh => hex value of the char
#----------------------------------

#Back Space
print("Hello\bWorld") #will remove one char which is o

#Escape New line + backslash \
print("Hello \
New \
World")

#Escape back slash
print("Hello\\World")

#Escape single quote
print("Hello \'  World")

#Escape double quote
print("Hello \"  World")

#line feed
print("Hello \nWorld")

#Carriage Return
print("Hello \rWorld")
print("123456\rabcd")
print("123456\rabcde")


#Horizontal Tab
print("Hello \tWorld")

#Hex value of Character
print("\x41\x6D\x69\x72\x61 ")
