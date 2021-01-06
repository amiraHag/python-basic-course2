# ----------------------------
# ------- List Methods -------
# ----------------------------

# append()

coursesList = ['Java', 'Python', 'Algorithm', 'Data']
oldCoursesList = ['C++', 'PHP','DataStructure']

coursesList.append('MatPlotlib')
coursesList.append(10)
coursesList.append(2.5)
coursesList.append(True)
print(coursesList)
coursesList.append(oldCoursesList)
print(coursesList)

# get value at specific index
print(coursesList[2])
print(coursesList[-1])
print(coursesList[:4])
print(coursesList[1:4])
print(coursesList[3:])
print(coursesList[-1][2])
print(coursesList[1][2])


# extend()

a=[1,2,3,4,5]
b=["A","B","C","D"]
c=["One","Two","Three"]
a.extend(b)
print(a)
a.extend(c)
print(a)


# remove()
x= [1,2,3,4,5,1,"A","B",True, "A",2,"A"]
x.remove("A")
print(x)


# sort()
y=[10,2,1,50,-10,0,4,8]
print(y)
y.sort()  # y.sort(reverse=False)
print(y)

y.sort(reverse=True)
print(y)

#y.append("amira")
#y.sort() ->  TypeError: '<' not supported between instances of 'str' and 'int'
#print(y)

z=["a","z","v","b"]
z.sort()
print(z)

# reverse()
n=[1,5,2,80,65,-10]
n.reverse()
print(n)
