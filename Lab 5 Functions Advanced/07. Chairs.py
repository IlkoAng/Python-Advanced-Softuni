import itertools
s = input().split(", ")
n = int(input())
for comb in itertools.combinations(s, n):
    print(', '.join(comb))