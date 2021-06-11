text = input()

mylist = [el for el in text if el not in "aouei"]
print(''.join(mylist))