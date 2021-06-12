command = input()
seq = [int(el) for el in input().split()]
filtered = []

if command == "Odd":
    filtered = filter(lambda num: num % 2 == 1, seq)
elif command == "Even":
    filtered = filter(lambda num: num % 2 == 0, seq)

print(sum(filtered) * len(seq))