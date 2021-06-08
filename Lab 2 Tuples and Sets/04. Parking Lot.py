n = int(input())
myset = set()

for _ in range(n):
    direct, reg = input().split(", ")
    if direct == "IN":
        if reg not in myset:
            myset.add(reg)

    elif direct == "OUT":
        if reg in myset:
            myset.remove(reg)

if len(myset) == 0:
    print("Parking Lot is Empty")
else:
    print(f"\n".join(myset))
