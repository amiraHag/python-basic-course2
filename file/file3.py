# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

file1 = open("amira.txt", "w")
file1.write("Hello \n")
file1.write("Amira \nSoftware Developer")
file1.close()
file2 = open(r"nfiles/fun.txt", "w")
file2.write("Amira\n" * 1000)
file2.close()

newList = ["Amira\n", "Software Developer\n", "30\n"]

file3 = open("amira.txt", "w")
file3.writelines(newList)
file3.close()
file4 = open("amira.txt", "a")
file4.write("Reading")
file4.close()
