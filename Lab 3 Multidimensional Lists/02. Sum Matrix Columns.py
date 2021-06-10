def read_matrix():
    r, c = input().split(", ")
    matrix = []
    for r_idx in range(int(r)):
        row = [int(el) for el in input().split()]
        matrix.append(row)
    return matrix


def get_column_sum(matrix):
    rows = len(matrix)
    col = len(matrix[0])
    sums = []

    for col_idx in range(col):
        col_sum = 0
        for row_idx in range(rows):
            col_sum += matrix[row_idx][col_idx]
        sums.append(col_sum)
    return sums


def print_result(values):
    [print(el) for el in values]


matrix = read_matrix()
result = get_column_sum(matrix)
print_result(result)


