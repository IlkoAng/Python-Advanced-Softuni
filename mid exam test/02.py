def is_valid_found(row, col):
    if 0 <= row < 7 and 0 <= col < 7:
        return True
    return False


def find_target(matrix, row, col):
    if is_valid_found(row, col):
        row_points = int(matrix[row][0]) + int(matrix[row][-1])
        col_points = int(matrix[0][col]) + int(matrix[-1][col])
        points = row_points + col_points

        return points


player_1, player_2 = input().split(", ")

matrix = []
for _ in range(7):
    line = input().split()
    matrix.append(line)

total_1 = 501
total_2 = 501
counter = 0
throws_1 = 0
throws_2 = 0
isWinner = False
while True:
    counter += 1
    coords = input()
    splitted = coords[1:-1].split(", ")
    r = int(splitted[0])
    c = int(splitted[1])
    if counter % 2 == 1:
        throws_1 += 1
    elif counter % 2 == 0:
        throws_2 += 1
    if is_valid_found(r, c):
        if matrix[r][c] == "D":
            points = find_target(matrix, r, c) * 2
            if counter % 2 == 1:
                total_1 -= points
                if total_1 <= 0:
                    isWinner = False
                    break
            elif counter % 2 == 0:
                total_2 -= points
                if total_2 <= 0:
                    isWinner = True
                    break
        elif matrix[r][c] == "T":
            points = find_target(matrix, r, c) * 3
            if counter % 2 == 1:
                total_1 -= points
                if total_1 <= 0:
                    isWinner = False
                    break
            elif counter % 2 == 0:
                total_2 -= points
                if total_2 <= 0:
                    isWinner = True
                    break
        elif matrix[r][c] == "B":
            if counter % 2 == 1:
                total_1 -= 501
                if total_1 <= 0:
                    isWinner = False
                    break
            elif counter % 2 == 0:
                total_2 -= 501
                if total_2 <= 0:
                    isWinner = True
                    break
        elif matrix[r][c].isdigit:
            points = find_target(matrix, r, c)
            if counter % 2 == 1:
                total_1 -= points
                if total_1 <= 0:
                    isWinner = False
                    break
            elif counter % 2 == 0:
                total_2 -= points
                if total_2 <= 0:
                    isWinner = True
                    break
if isWinner:
    print(f"{player_2} won the game with {throws_2} throws!")
if not isWinner:
    print(f"{player_1} won the game with {throws_1} throws!")








