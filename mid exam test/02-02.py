def is_in_range(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


n = int(input())
matrix = []
start_position = None

for row in range(n):
    rows = input().split()
    if "P" in rows:
        start_position = [row, rows.index("P")]
    matrix.append(rows)

commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

coins = 0
path = []

while True:
    command = input()
    if command in commands:
        new_row = start_position[0] + commands[command][0]
        new_col = start_position[1] + commands[command][1]
        if is_in_range(new_row, new_col, n) and not matrix[new_row][new_col] == "X":
            coins += int(matrix[new_row][new_col])
            path.append([new_row, new_col])
        else:
            coins //= 2
            print(f"Game over! You've collected {coins} coins.")
            break
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break
        start_position = [new_row, new_col]

print(f"Your path: ")
[print(step) for step in path]


