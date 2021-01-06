#------------------------------------
#-------Indexing and Slicing---------
#------------------------------------
# [1] All Data in Python is Object
# [2] Obect Contain elements
# [3] Every element has it is own index
# [4] Python use zero based indexing (index start from zero)
# [5] use the square brackets to access the elements
# [6] Indexing and slicing -> system enable us to access part of strings, tuples or list
#------------------------------------


#Indexing => access single element
my_name = "Amira Mustafa"
print(my_name[0]) #print index 0 => A
print(my_name[8]) #print index 8 => s

#Negative Indexing access element from the right (from the end)
print(my_name[-2]) #print index -2 => f


#Slicing => access group of sequence elements
#[Start:End] start include and end execlude
#start optional if not added it will be 0
#end optional if not added it will be the end of elements
#if start and end empty the full elements will display
#[Start:End:Steps]
#steps optional if not included it will be 1

print(my_name[6:9]) #print Mus
print(my_name[3:5]) #print ra

print(my_name[:3]) #print Ami
print(my_name[9:]) #print tafa
print(my_name[:]) #print full string

print(my_name[0::1]) # print full string
print(my_name[0:10:2]) #print AiaMs 1st chat then 3rd then fifth each time increase 2 not one as default
print(my_name[0:12:3]) #print ArMt
