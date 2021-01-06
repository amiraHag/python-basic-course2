# ----------------------------
# ------- List Methods -------
# ----------------------------


# clear()
a=[1,2,3,4,5]
print(a)
a.clear()
print(a)

# copy()
b = [1,2,3,4]
c= b.copy()
print(b)
print(c)
b.append(5)
print(b)
print(c)

# count()
d=[1,3,4,2,2,5,2,3,2]
print(d.count(2))

# index()
e=["A","B","C","D","E","F","A","C","A"]
print(e.index("B"))
print(e.index("A"))


# insert()
f=[1,5,2,90,14,76,32,71]
f.insert(0,-10)
print(f)
f.insert(-1,120)
print(f)


# pop()
g=[1,2,3,4,5,6,7]
print(g.pop(3))
print(g.pop(-1))
print(g)
