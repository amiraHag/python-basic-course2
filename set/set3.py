# -------------------------------
# --------- Set Methods ---------
# -------------------------------


# difference() return the values in the first set that not in the second set
set1 ={1, 2, 3, 4, 5, 6, 7, 8 , 9}
set2 = {1, 2, 3, 4, 5, 6, "A", "B"}
print(set1)
print(set2)
print(set1.difference(set2))
print(set1-set2)
print(set2.difference(set1))
print(set2-set1)
print(set1)
print(set2)

print("*" * 40)

# difference_update() return the values in the first set that not in the second set
# and update the value for the first set with this values
set3 ={1, 2, 3, 4, 5, 6, 7, 8 , 9}
set4 = {1, 2, 3, 4, 5, 6, "A", "B"}
print(set3)
set3.difference_update(set4)
print(set3)
print("*" * 40)

# intersection() return the values in the first set and in the second set
set5 ={1, 2, 3, 4, 5, 6, 7, 8 , 9}
set6 = {1, 2, 3, 4, 5, 6, "A", "B"}
print(set5)
print(set5.intersection(set6))
print(set5)
print("*" * 40)

# intersection_update() return the values in the first set and in the second set
# and update the value for the first set with this values
set7 ={1, 2, 3, 4, 5, 6, 7, 8 , 9}
set8 = {1, 2, 3, 4, 5, 6, "A", "B"}
print(set7)
set7.intersection_update(set8)
print(set7)
print("*" * 40)

# symmetric_difference() return the values in the first set and not in the second set
# and the values in the second set and not in the first set
set9 ={1, 2, 3, 4, 5, 6, 7, 8 , 9}
set10 = {1, 2, 3, 4, 5, 6, "A", "B"}
print(set9)
print(set9.symmetric_difference(set10))
print(set9^set10)
print(set9)
print("*" * 40)

# symmetric_difference_update() return the values in the first set and not in the second set
# and the values in the second set and not in the first set
# and update the value for the first set with this values
set11 ={1, 2, 3, 4, 5, 6, 7, 8 , 9}
set12 = {1, 2, 3, 4, 5, 6, "A", "B"}
print(set11)
set11.symmetric_difference_update(set12)
print(set11)
print("*" * 40)
