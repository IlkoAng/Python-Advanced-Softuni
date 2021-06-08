n = int(input())
myset = set()
for _ in range(n):
    elements = input().split()
    for el in elements:
        myset.add(el)
print("\n".join(myset))