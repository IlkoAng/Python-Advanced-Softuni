from collections import deque

n_water = int(input())
names = input()
people = deque()
while not names == "Start":
    people.append(names)

    names = input()

command = input()
while not command == "End":
    if command.isnumeric():
        if n_water >= int(command):
            n_water -= int(command)
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    else:
        action, quantity = command.split()
        n_water += int(quantity)

    command = input()

print(f"{n_water} liters left")
