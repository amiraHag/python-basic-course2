#------------------------------------
#----------String Methods------------
#------------------------------------

# replace(old_value, new_value, count)
a= "Hello One Two Three Four One One"
print(a)
print(a.replace("One","1"))
print(a.replace("One","1",1))
print(a.replace("One","1",2))

# separator.join(Iterable) -> Iterable object can iterate on
b=["one","two","three","four","five"]
print(" ".join(b))
print("_".join(b))
print(type("_".join(b)))
