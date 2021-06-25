import os

try:
    os.remove("asd.txt")
except FileNotFoundError:
    print("File already deleted!")