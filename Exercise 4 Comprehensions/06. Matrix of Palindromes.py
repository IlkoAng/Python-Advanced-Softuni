
r, c = input().split()
r = int(r)
c = int(c)

main = 97


def generate_element(row, col):
    first = chr(main + row)
    middle = chr(main + row + col)
    return f"{first}{middle}{first}"


matrix =[[generate_element(row, col) for col in range(c)] for row in range(r)]

print('\n'.join(' '.join([str(word) for word in el]) for el in matrix))

