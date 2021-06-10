def read_matrix():
    r, c = input().split(", ")
    matrix = []
    for rr_idx in range(int(r)):
        row = [int(el) for el in input().split(", ")]
        matrix.append(row)
    return matrix


def submatrix_sum(matrix, row_idx, col_idx, size):
    the_sum = 0
    for r in range(row_idx, row_idx+size):
        for c in range(col_idx, col_idx+size):
            the_sum += matrix[r][c]
    return the_sum


def best_submatrix_sum(matrix, submatrix_size):
    best_row = 0
    best_col = 0
    best_sum = submatrix_sum(matrix, 0, 0, submatrix_size)
    for r_idx in range(len(matrix) - submatrix_size + 1):
        for c_idx in range(len(matrix[r_idx]) - submatrix_size + 1):
            current_sum = submatrix_sum(matrix, r_idx, c_idx, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row = r_idx
                best_col = c_idx
    return (best_row, best_col)


def print_result(coordinates, size):
    row_index, col_index = coordinates
    for r in range(row_index, col_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(submatrix_sum(matrix, row_index, col_index, size))


submatrix_size = 2
matrix = read_matrix()
coordinates = best_submatrix_sum(matrix, submatrix_size)