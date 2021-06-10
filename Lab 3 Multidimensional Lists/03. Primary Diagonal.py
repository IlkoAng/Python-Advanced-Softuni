def read_matrix():
    r = int(input())
    matrix = []
    for r_idx in range(int(r)):
        row = [int(el) for el in input().split()]
        matrix.append(row)
    return matrix


matrix = read_matrix()


def sum_diagonal(matrix):
    sum_of_diagonal = 0
    for idx in range(len(matrix)):
        sum_of_diagonal += matrix[idx][idx]
    return sum_of_diagonal


print(sum_diagonal(matrix))