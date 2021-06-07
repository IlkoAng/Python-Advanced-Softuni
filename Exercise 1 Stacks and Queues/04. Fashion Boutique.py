clothes_value = list(map(int, input().split()))
capacity = int(input())
sum = 0
counter = 0
for idx in range(len(clothes_value)-1, -1, -1):
    sum += clothes_value[idx]
    if sum <= capacity:
        clothes_value.pop()
    else:
        counter += 1
        sum = clothes_value[idx]

if sum > 0:
    counter += 1

print(counter)