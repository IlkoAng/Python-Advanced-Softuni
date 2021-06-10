def create_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append([int(el) for el in input().split()])

    return matrix


matrix = create_matrix()


def get_coordinates():
    coords = input().split()
    bomb_coords = []
    for idx in range(len(coords)):
        current_cord = tuple(map(int, coords[idx].split(",")))
        bomb_coords.append(current_cord)

    return bomb_coords

def detonate_bomb(matr, coords):
    row, col = coords
    bomb_value = matr[row][col]
    reduce_cords = [
        (row, col), (row-1, col-1), (row-1, col), (row-1, col+1),
        (row, col-1), (row, col+1), (row+1, col-1), (row+1, col),
        (row+1, col+1)
    ]
    for cell in reduce_cords:
        row_index, col_index = cell
        if bomb_value > 0:
            if 0 <= row_index < len(matr) and 0 <= col_index < len(matr):
                matr[row_index][col_index] -= bomb_value


coordinates = get_coordinates()

for idx in range(len(coordinates)):
    current_bomb = coordinates[idx]
    detonate_bomb(matrix, current_bomb)







