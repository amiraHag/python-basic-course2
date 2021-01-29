# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------

# sum(iterable, start)
# start default 0
a = [1, 2, 3, 4]
print(sum(a))
print(sum(a, 100))


# round(number, numofdigits)
# default round to the integer value
# number of digits default none digits
print(round(1.23456))
print(round(1.23456, None))
print(round(1.23456, 2))

# range(start, end, step)
# start optional default 0
# end mandatory
# step optional default 1
print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))

# print()
print("Hello Amira, How Are You")
print("Hello", "Amira", "How", "Are", "You", sep=" | ")

print("First Line", end=" ")
print("Second Line")
print("Third Line")
