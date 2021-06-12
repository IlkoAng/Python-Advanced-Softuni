def is_even(num):
    return num % 2 == 0


seq = [int(el) for el in input().split()]
print(list(filter(is_even, seq)))



