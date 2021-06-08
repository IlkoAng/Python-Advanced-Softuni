name = input()
mydict = {}

for el in name:
    mydict[el] = name.count(el)

sorted_data = sorted(mydict.items(), key=lambda x: x[0])
for key in sorted_data:
    print(f"{key[0]}: {key[1]} time/s")