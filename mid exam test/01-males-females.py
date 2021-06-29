from collections import deque

males = [int(el) for el in input().split()]
males = [el for el in males if el > 0]
females = [int(el) for el in input().split()]
females = deque([el for el in females if el > 0])
matches = 0

while True:
    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue
    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if males[-1] == females[0]:
        males.pop()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.remove(-1)
    if len(males) <= 0 or len(females) <= 0:
        break

males = [str(el) for el in males]
males.reverse()
females = [str(el) for el in females]
print(f"Matches: {matches}")
if males:
    print(f'Males left: {", ".join(males)}')
else:
    print(f'Males left: none')
if females:
    print(f'Females left: {", ".join(females)}')
else:
    print(f'Females left: none')