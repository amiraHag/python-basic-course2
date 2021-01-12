# -------------------------------
# --------- Set Methods ---------
# -------------------------------

# issuperset() return true if the set contains all elements in the second set
set1 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
set2 = { 1, 2, 3, 4 }
set3 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
set4 = { "A", "B", "C" }

print(set1.issuperset(set2))
print(set1.issuperset(set3))
print(set1.issuperset(set4))
print("*"*40)

# issubset() return true if the set contains part of the elements in the second set
set5 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
set6 = { 1, 2, 3, 4 }
set7 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set8 = { "A", "B", "C" }

print(set6.issubset(set5))
print(set7.issubset(set5))
print(set8.issubset(set5))
print("*"*40)

# isdisjoint() return true if the set didn't contains any of the elements in the second set
set9 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
set10 = { 1, 2, 3, 4 }
set11 = { "A", "B", "C" }

print(set9.isdisjoint(set10))
print(set9.isdisjoint(set11))
print("*"*40)
