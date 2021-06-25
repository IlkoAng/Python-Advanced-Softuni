from os import path

if path.exists("file.txt"):
    print("File found")
else:
    print("File not found")