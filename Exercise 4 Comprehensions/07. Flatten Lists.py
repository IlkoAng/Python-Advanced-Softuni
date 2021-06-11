data = input().split("|")

data = [el.split() for el in data]
data.reverse()

data = [number for seq in data for number in seq]

print(' '.join(data))