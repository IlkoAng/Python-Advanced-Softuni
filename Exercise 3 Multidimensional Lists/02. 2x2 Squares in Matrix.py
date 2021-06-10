r, c = [int(el) for el in input().split()]
matrix = []
for _ in range(r):
    row = input().split()
    matrix.append(row)

counter = 0
for r_idx in range(r-1):
    for c_idx in range(c-1):
        current_el = matrix[r_idx][c_idx]
        next_el = matrix[r_idx][c_idx+1]
        below_el = matrix[r_idx+1][c_idx]
        below_next_el = matrix[r_idx+1][c_idx+1]
        if current_el == next_el and next_el == below_el and below_el == below_next_el:
            counter += 1

print(counter)

