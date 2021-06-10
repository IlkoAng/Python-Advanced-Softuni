size = int(input())
matrix = []
for _ in range(size):
    row = [int(el) for el in input().split()]
    matrix.append(row)

primary_sum = 0
secondary_sum = 0
for idx in range(len(matrix)):
    primary_sum += matrix[idx][idx]
    secondary_sum += matrix[idx][size - idx - 1]

the_sum = abs(primary_sum - secondary_sum)
print(the_sum)