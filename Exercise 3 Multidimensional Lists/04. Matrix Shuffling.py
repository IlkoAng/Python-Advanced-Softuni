r, c = [int(el) for el in input().split()]


def init_matrix(r,c):
    matrix = []
    for _ in range(r):
        row = input().split()
        matrix.append(row)
    return matrix


def check_valid_index(index_row, index_col, rows, cols):
    if 0 <= index_row < rows and 0 <= index_col < cols:
        return True
    return False


def check_valid_command(command, cords, rows, cols):
    if len(cords) == 4 and command == "swap":
        for index in range(0, len(cords), 2):
            if not check_valid_index(cords[index], cords[index+1], rows, cols):
                print("Invalid input!")
                return False
        return True
    print("Invalid input!")
    return False


def print_matrix(matr):
    for row_index in range(len(matr)):
        for col_index in range(len(matr[row_index])):
            print(f"{matr[row_index][col_index]} ", end='')
        print()


matrix = init_matrix(r, c)


data = input()

while not data == "END":
    try:
        splitted_data = data.split()
        command = splitted_data[0]
        coordinates = [int(el) for el in splitted_data[1:]]
    except:
        print("Invalid input!")
    if check_valid_command(command, coordinates, r, c):
        current_row = coordinates[0]
        current_col = coordinates[1]
        row_to_swap = coordinates[2]
        col_to_swap = coordinates[3]
        temp = matrix[current_row][current_col]
        matrix[current_row][current_col] = matrix[row_to_swap][col_to_swap]
        matrix[row_to_swap][col_to_swap] = temp
        print_matrix(matrix)

    data = input()

