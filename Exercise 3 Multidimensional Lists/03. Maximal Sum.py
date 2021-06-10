import sys

r, c = [int(el) for el in input().split()]
matrix = []
for _ in range(r):
    row = [int(el) for el in input().split()]
    matrix.append(row)

submatrix = []
the_sum = -sys.maxsize
best_curr_el = 0
best_above_left_el = 0
best_above_mid_el = 0
best_above_right_el = 0
best_left_el = 0
best_right_el = 0
best_below_left_el = 0
best_below_mid_el = 0
best_below_right_el = 0

for r_idx in range(1, r-1):
    for c_idx in range(1, c-1):
        curr_el = matrix[r_idx][c_idx]
        above_left_el = matrix[r_idx-1][c_idx-1]
        above_mid_el = matrix[r_idx-1][c_idx]
        above_right_el = matrix[r_idx-1][c_idx+1]
        left_el = matrix[r_idx][c_idx-1]
        right_el = matrix[r_idx][c_idx+1]
        below_left_el = matrix[r_idx+1][c_idx-1]
        below_mid_el = matrix[r_idx+1][c_idx]
        below_right_el = matrix[r_idx+1][c_idx+1]
        current_sum = curr_el + above_left_el + above_mid_el + above_right_el + left_el + right_el + below_left_el + below_mid_el + below_right_el
        if the_sum < current_sum:
            the_sum = current_sum
            best_curr_el = curr_el
            best_above_left_el = above_left_el
            best_above_mid_el = above_mid_el
            best_above_right_el = above_right_el
            best_left_el = left_el
            best_right_el = right_el
            best_below_left_el = below_left_el
            best_below_mid_el = below_mid_el
            best_below_right_el = below_right_el

print(f"Sum = {the_sum}")
print(f"{best_above_left_el} {best_above_mid_el} {best_above_right_el}")
print(f"{best_left_el} {best_curr_el} {best_right_el}")
print(f"{best_below_left_el} {best_below_mid_el} {best_below_right_el}")
