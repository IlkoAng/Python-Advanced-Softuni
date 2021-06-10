def read_matrix():
    r, c = input().split(", ")
    matrix = []
    for r_idx in range(int(r)):
        row = [int(el) for el in input().split(", ")]
        matrix.append(row)
    return matrix


matrix_sum = 0
matrix = read_matrix()

for r in range(len(matrix)):
    matrix_sum += sum(matrix[r])

print(matrix_sum)
print(matrix)
