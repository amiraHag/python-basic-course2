# ------------------------
# -- Built In Functions --
# ------------------------
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------

# abs() absolute value
print(abs(1))
print(abs(-1))
print(abs(1.123))
print(abs(-1.123))

print("*" * 40)

# pow(base, exp, mod) base to the power exp modulus mod
print(pow(2, 5))  # 2 to the power 5 (2^5)
print(pow(2, 5, 10))  # 2 to the power 5 modulus 10 (2 ^ 5) % 10

print("*" * 40)

# min(item, item , item, or iterator)
myList = (1, 2, -40, 5, -10, 100)
print(min(1, 2, -40, 5, -10, 100))
print(min("X", "A", "C", "c", "B", "Amira"))
print(min(myList))

print("*" * 40)

# max(item, item , item, or iterator)
myList = (1, 2, -40, 5, -10, 100)
print(max(1, 2, -40, 5, -10, 100))
print(max("X", "A", "C", "c", "B", "Amira"))
print(max(myList))

print("*" * 40)

# slice(start, end, step)
a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])
