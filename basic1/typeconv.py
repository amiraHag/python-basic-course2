# ---------------------
# -- Type Conversion --
# ----------------------

# str()

a = 23
print(type(a))
print(type(str(a)))

print("*" * 50)


# tuple()

myString = "Amira"
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mySet = {"A", "B", "C", "D", "E", "F", "G"}
myDict = {"A": 1, "B": 2, "C": 3}

# print(tuple(a)) Error -> TypeError: 'int' object is not iterable
print(tuple(myString))
print(tuple(myList))
print(tuple(mySet))
print(tuple(myDict))
print("*" * 50)


# list()

myString = "Amira"
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
mySet = {"A", "B", "C", "D", "E", "F", "G"}
myDict = {"A": 1, "B": 2, "C": 3}

# print(list(a)) Error -> TypeError: 'int' object is not iterable
print(list(myString))
print(list(myTuple))
print(list(mySet))
print(list(myDict))
print("*" * 50)

# set()

myString = "Amira"
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
myList = ["A", "B", "C", "D", "E", "F", "G"]
myDict = {"A": 1, "B": 2, "C": 3}

# print(set(a)) Error -> TypeError: 'int' object is not iterable
print(set(myString))
print(set(myTuple))
print(set(myList))
print(set(myDict))
print("*" * 50)

# dict()
myString = "Amira"
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
myList = ["A", "B", "C", "D", "E", "F", "G"]
mySet = {"A", "B", "C", "D", "E", "F", "G"}
myTuple2 = (("A", 1), ("B", 2), ("C", 3))
myList2 = [["One", 1], ["Two", 2], ["Three", 3]]

# print(dict(myString)) ValueError: dictionary update sequence element #0 has length 1; 2 is required
# print(dict(myTuple)) TypeError: cannot convert dictionary update sequence element #0 to a sequence
# print(dict(myList)) ValueError: dictionary update sequence element #0 has length 1; 2 is required
# print(dict(mySet)) ValueError: dictionary update sequence element #0 has length 1; 2 is required
print(dict(myTuple2))
print(dict(myList2))
