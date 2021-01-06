#----------------------------------
# -- Variables --
#----------------
# Syntax => [Variable Name] [Assigment Operator] [Value]
#
#Name Convention and Rules
# [1] can start by (a-z) (A-Z) or (_) underscore
# [2] can't start with number or special char
# [3] can include numbers 0-9 or underscore
# [4] can't include special char
# [5] case sensitive (name not like Name)
#
#use
#can't use variable before assign
#
#Best Practise in variable Name
# single word => lowercase
# two words => use camel case (camelCase)
# two words => use snake case (snake_case)
#----------------------------------



myVariable = 'my value'

_myVariable = 'my value'

MyVariable = 'my value'

#1myVariable = 'myvalue'  => invalid syntax error

#@myVariable = 'myvalue'  => invalid syntax error

my12Variable = 'myvalue'
my_Variable = 'myvalue'

#my@Variable = 'myvalue'  => invalid syntax error

#print(Name) => error variable not defined
name = "a"  #one word => normal
Name = "b"

myName ="aa" #two words => camelCase
my_name ="aa" #two words => snake_case
