# ------------------------
# -- Built In Functions --
# ------------------------
# all()
# any()
# bin()
# id()
# ------------------------

list1 = [1, 2, 3, 4, 5, True]
#list1 = [1, 2, 3, 4, 5, False]

if all(list1):
    print("All list items true")
else:
    print("List1 contain one or more false element")

#list1 = [0, False]
if any(list1):
    print("One or More elemets true")
else:
    print("List1 not contain any true element")

print(bin(100))

a = 1
b = 20

print(id(a))
print(id(b))
