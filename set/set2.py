# -------------------------------
# --------- Set Methods ---------
# -------------------------------

# clear() remove all elements from the set
set1 = { 1, 2, 3, 4, 5, 6 }
print(set1)
set1.clear()
print(set1)

# union() combine sets together
a = { 1, 2, 3, 4, 5, 6 }
b = { "A", "B", "C" }
c = b.union(a) # comine a and b and put it in c but a and b not affected
print(b)
print(a)
print(b | a)
print(b.union(a))
print(c)
d = {"D", "E", "F"}
print(b.union(a,d)) # You can comine more than two sets

# add() add one element to the set
d.add("G")
d.add("H")
print(d)
# d.add("G","H") TypeError: add() takes exactly one argument (2 given)
# print(d)


# copy()
# Make a shallow copy
# This means the new set will now be a new and independent object with the same contents as the original one.
e = {1, 2, 3, 4, 5, 6, 7}
f = e.copy()
print(e)
print(f)

e.add(9)
print(e)
print(f)

# remove()

g = { "A", "B", "C", "D", "E" }
# g.remove(1) Key Error that is because the element not in the set
g.remove("A")
print(g)

# discard() remove elemnt like remove function but not issue error if the element not found

h = { "A", "B", "C", "D", "E" }
h.discard(1) # Not do anything if the element not in the list
h.discard("A")
print(h)


# pop() return random element from the set

i = {"A", "B", "C", "D", True, 1, 2, 3, 4, 5}
print(i.pop())

# update() add elements to the set with another set or any iterable object
j = {1, 2, 3, 4, 5}
k = {"A", "B", "C", "D", 2, 9}
j.update(k)
j.update(['Amira', "Hag"])
j.update({'Amira', "Hag"})
j.update('Amira', "Hag") # this will add each character as separte element because it use it as iterable object not string
j.update([10, 11])
j.update({12, 13})
print(j)
