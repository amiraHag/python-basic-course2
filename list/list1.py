# --------------------------------------------------

# ---------------------
# ------- Lists -------
# ---------------------

# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types

# --------------------------------------------------

myList = ["one", "two", "three", "one","o", 1, 1.2, True]
print(myList)

# Access the items in the list using the index -> python zero based indexing
print(myList[2])
print(myList[-1])


# Slicing the List
print(myList[2:5])
print(myList[4:])
print(myList[4:-2])
print(myList[:-3])

# Slicing the list using start, stop and step
print(myList[::1])
print(myList[::2])
print(myList[2:7])
print(myList[2:7:2])
print(myList[::2])
print(myList[::3])

# Change the elemnets value in the list
print(myList)
myList[1] ="Amira"
myList[6] =30
myList[-1] =False
print(myList)
myList[2:4]=[2,3]
print(myList)
myList[4:6]=[]
print(myList)
myList[0:2]=['A']
print(myList)
