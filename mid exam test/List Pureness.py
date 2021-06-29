from collections import deque


def best_list_pureness(numbers, k):
    data = {}
    result = 0
    numbers = deque(numbers)
    for rotation in range(k+1):
        result = sum([index * value for index, value in enumerate(numbers)])
        data[rotation] = result
        numbers.appendleft(numbers.pop())

    max_pureness = max(data.values())
    for key, value in data.items():
        if max_pureness == value:
            return f"Best pureness {value} after {key} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

