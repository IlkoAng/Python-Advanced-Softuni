from collections import deque

effects = deque([int(el) for el in input().split(", ")])
filtered_effects = deque(list(filter(lambda num: 0 < num, effects)))
powers = [int(el) for el in input().split(", ")]
filtered_power = list(filter(lambda num: 0 < num, powers))
palm = 0
willow = 0
crossette = 0
isDone = False
while len(filtered_effects) > 0 and len(filtered_power) > 0:
    effect = filtered_effects.popleft()
    if effect <= 0:
        if len(filtered_effects) == 0:
            break
        continue
    power = filtered_power.pop()
    if power <= 0:
        if len(filtered_power) == 0:
            break
        filtered_effects.appendleft(effect)
        continue
    if (effect + power) % 3 == 0 and (effect + power) % 5 != 0:
        palm += 1
    elif (effect + power) % 5 == 0 and (effect + power) % 3 != 0:
        willow += 1
    elif (effect + power) % 3 == 0 and (effect + power) % 5 == 0:
        crossette += 1
    elif (effect + power) % 3 != 0 and (effect + power) % 5 != 0:
        effect -= 1
        filtered_effects.append(effect)
        filtered_power.append(power)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        isDone = True
        break


if isDone:
    print("Congrats! You made the perfect firework show!")

if not isDone:
    print("Sorry. You can't make the perfect firework show.")

if len(filtered_effects) > 0:
    filtered_effects = [str(el) for el in filtered_effects]
    print(f"Firework Effects left: {', '.join(filtered_effects)}")
if len(filtered_power) > 0:
    filtered_power = [str(el) for el in filtered_power]
    print(f"Explosive Power left: {', '.join(filtered_power)}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")