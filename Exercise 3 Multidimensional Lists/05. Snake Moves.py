r, c = [int(el) for el in input().split()]

word = input()
matrix = []

for row_index in range(r):
        matrix.append([0 for el in range(c)])

index_word = 0

for row_index in range(r):
    for col_index in range(c):
        matrix[row_index][col_index] = word[index_word]
        index_word += 1
        if index_word == len(word):
            index_word = 0

for row_index in range(r):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    print(''.join(matrix[row_index]))