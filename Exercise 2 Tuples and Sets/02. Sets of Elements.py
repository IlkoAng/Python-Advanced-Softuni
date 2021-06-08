n, m = [int(el) for el in input().split()]
first = set()
second = set()

for _ in range(n):
    first.add(input())
for _ in range(m):
    second.add(input())

print("\n".join(first.intersection(second)))