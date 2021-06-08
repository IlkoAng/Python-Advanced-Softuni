n = int(input())
myset = set()
for _ in range(n):
    name = input()
    if name not in myset:
        print(name)
        myset.add(name)
