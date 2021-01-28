# --------------------------------
# -- File Handling => Read File --
# --------------------------------

file1 = open("amira.txt","r")

# get the data of the file
print(file1)

print(file1.name)
print(file1.mode)
print(file1.encoding)
print("*" * 40)

# read the content of the file
# read() accept the number of bytes you want to read from the file default value -1 that read all content

print(file1.read(3))
print("*" * 40)
print(file1.read())
print("*" * 40)
print(file1.readline(5))
print(file1.readline())
print(file1.readline())

print(file1.readlines())
print(file1.readlines(50))
print(type(file1.readlines()))

for line in file1:

  print(line)

  if line.startswith("07"):

    break
file1.close()
