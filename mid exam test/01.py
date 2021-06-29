from collections import deque

orders = [int(el) for el in input().split(", ")]
filtered = deque(list(filter(lambda num: 0 < num <= 10, orders)))
capacity = [int(el) for el in input().split(", ")]
pizza = 0

while filtered:
    if len(capacity) == 0:
        break
    order = filtered.popleft()
    if order >= capacity[-1]:
        while order > 0:
            if len(capacity) == 0:
                filtered.appendleft(order)
                break
            if order <= capacity[-1]:
                capacity[-1] -= order
                pizza += order
                order = 0
            elif order > capacity[-1]:
                order -= capacity[-1]
                pizza += capacity[-1]
            capacity.pop(-1)
    elif order < capacity[-1]:
        capacity.pop(-1)
        pizza += order

filtered = [str(el) for el in filtered]
capacity = [str(el) for el in capacity]

if len(filtered) > 0:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(filtered)}")

else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizza}")
    print(f"Employees: {', '.join(capacity)}")