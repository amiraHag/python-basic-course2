# ------------------------------------------------------------
#
# -----------------------
# -------- Tuple --------
# -----------------------
#
#
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# ------------------------------------------------------------


# Tuple Syntax & Type
myTuple1 = ("Amira","Hag")
print(type(myTuple1))
print(myTuple1)

myTuple2 = "Amira","Hag"
print(type(myTuple2))
print(myTuple2)

# Tuple Indexing
tupleNumbers = (1,2,3,4,5,6,7)
print(tupleNumbers[0])
print(tupleNumbers[-1])
print(tupleNumbers[2])
print(tupleNumbers[1:5])

# Tuple Assign Values
tupleNumbers2 = (1,2,3,4,5,6,7,8,9,10)
# tupleNumbers2[2] = 11 -> Error: TypeError: 'tuple' object does not support item assignment
# print(tupleNumbers2)


# Tuple Data
myTuple3 = ("Amira","Hag" ,1,2,True, 5,1,2.3,-12,"M")
print(myTuple3[4])
print(myTuple3[-2])
