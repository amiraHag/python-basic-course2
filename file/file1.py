# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

import os

file = open("amira.txt") # r is the default mode "r"
file2= open(r"nfiles/amira.txt") #r"" means that the text is raw string

# Main Current Working Directory
print(os.getcwd())

# Path For The Opened File
print(os.path.abspath(__file__))

# Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

print(os.path.abspath(__file__))
