# ---------------------------------------------------------------------------------------
#
# -----------------------
# --------- Set ---------
# -----------------------
#
#
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# ---------------------------------------------------------------------------------------

# used {} not [] like lists or () like tuples
set1 = {"Amira",100,True,2,30,4,5,6,7,8}

# Set items Not Ordered And Not Indexed NOt Slicing
print(set1)
#print(set1[2]) Error -> TypeError: 'set' object does not support indexing
#print(set1[1:3]) Error -> TypeError: 'set' object is not subscriptable


# Set elements from Only Immutable Data Types

#mySet2 = {"Amira", 4, 1.5, True, [1, 2, 3]} # Eror -> TypeError: unhashable type: 'list'
#print(mySet2)

mySet3 = {"Amira", 4, 1.5, True, (1, 2, 3)}
print(mySet3)


# Set Items Is Unique

mySet4 = {1, 2, "A", "B", "A", True, 54, 2} # Will remove the repeated version of the element
print(mySet4)
