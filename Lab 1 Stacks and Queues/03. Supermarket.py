from collections import deque

command = input()
que = deque()

while not command == "End":
    if command == "Paid":
        while len(que):
            print(que.popleft())
    else:
        que.append(command)

    command = input()

print(f"{len(que)} people remaining.")