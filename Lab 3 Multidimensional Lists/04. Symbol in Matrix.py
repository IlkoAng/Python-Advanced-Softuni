def read_matrix():
    r = int(input())
    matrix = []
    for r_idx in range(r):
        row = [el for el in input()]
        matrix.append(row)
    return matrix


matrix = read_matrix()
symbol = input()


def find_symbol(matrix, symbol):
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            current_symbol = matrix[row_idx][col_idx]
            if current_symbol == symbol:
                return row_idx, col_idx


def print_result(result, symbol):
    if result:
        print(result)
    else:
        print(f"{symbol} does not occur in the matrix")


print_result(find_symbol(matrix, symbol), symbol)

