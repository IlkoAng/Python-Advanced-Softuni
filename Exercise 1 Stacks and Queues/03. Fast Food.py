from collections import deque

whole_qty = int(input())
orders = deque(map(int, input().split()))
print(max(orders))


while orders:
    order = orders.popleft()
    if whole_qty >= order:
        whole_qty -= order
    else:
        orders.appendleft(order)
        break

orders = list(map(str, orders))
if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(orders)}")

