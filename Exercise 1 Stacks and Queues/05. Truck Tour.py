from collections import deque
pump_nums = int(input())
myque = deque()
temp_q = deque()

for _ in range(pump_nums):
    pump_data = list(map(int, input().split()))
    myque.append(pump_data[0] - pump_data[1])

total_fuel = 0
idx = -1

while len(myque) > 0:
    pump = myque.popleft()
    total_fuel += pump
    idx += 1

    if total_fuel < 0:
        total_fuel = 0
        while len(temp_q) > 0:
            myque.append(temp_q.popleft())
    else:
        temp_q.append(idx)
print(temp_q[0])

