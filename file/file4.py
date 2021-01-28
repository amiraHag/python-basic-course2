# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------
import os


file1 = open("amira.txt", "a")
file1.truncate(23)
file1.close()

file2 = open("amira.txt", "a")
print(file2.tell())
file2.close()

file3 = open("amira.txt", "r")
file3.seek(6)
print(file3.read())
file3.close()
os.remove("nfiles/amira.txt")
