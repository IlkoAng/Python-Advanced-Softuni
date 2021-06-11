n = int(input())
matrix = []
for _ in range(n):
    matrix.append(int(el) for el in input().split(", "))

flatted = [num for submatrix in matrix for num in submatrix]
print(flatted)