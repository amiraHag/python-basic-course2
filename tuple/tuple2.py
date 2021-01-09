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

# Tuple With One Element
myTuple1 = ("Amira")
print(type(myTuple1))
print(myTuple1)

myTuple2 = "Amira"
print(type(myTuple2))
print(myTuple2)

# To avoid read as string , put , after the Element
myTuple1 = ("Amira",)
print(type(myTuple1))
print(myTuple1)

myTuple2 = "Amira",
print(type(myTuple2))
print(myTuple2)

# len() function to know how many Elements in Tuple
print(len(myTuple1))
print(len(myTuple2))

# Tuple Concatenation

a = (1, 2, 3, 4, 5, 6, 7)
b = (11, 12, 13, 14, 15)

c = a + b
d = a + ("A", "B","C","D",1.2, True) + b

print(c)
print(d)


# * Repeat for  Tuple, List, String  are the same

myString = "ABC"
myList = [1, 2, 3, 4, 5]
myTuple = ("A", "B", "C")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# count() method count the value in the tuple
e=(1,2,3,4,5,6,2,45,2,6,2)
print(e.count(2))
print(e.count(6))
print(e.count(45))

# index() method get the value at the given Index
f=(1,2,3,4,5,8,10,14,16)
print(f"The index for the element value 10 %d" % f.index(10))
print("The index for the element value 10 {:d}".format(f.index(10)))
print(f"The index for the element value 10 {f.index(10)}")

# Destruct
g = ("A","B","C")
x1,y1,z1 = g
print(x1)
print(y1)
print(z1)
g1 = ("A","B",67,"C")
x2,y2,_,z2 = g1
print(x2)
print(y2)
print(z2)
