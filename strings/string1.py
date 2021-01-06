#---------------------
#-------Strings-------
#---------------------

myString = 'This is Single Quote Variable'
my_string = "This is Double Quotes Variable"
print(myString)
print(my_string)

#reverse single and double quote in string to avoid \
my_string_one = 'This is "Test"'
my_string_two = "This is 'Test'"
print(my_string_one)
print(my_string_two)


#print multiple lines use triple single quote ''' or triple double quote """
#it also scape single and double quotes, it also work as scape char but only if the scape \ followed by text
my_string_three="""First
Second 'Test' "Test"
Third"""
my_string_four='''First
Second 'Test' \\\ "Test" \
Third'''
print(my_string_three)
print(my_string_four)
