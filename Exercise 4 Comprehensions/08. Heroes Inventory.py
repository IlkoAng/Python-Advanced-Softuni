names = input().split(", ")
inventory = {hero:{} for hero in names}
command = input()

while not command == "End":
    hero, item, price = command.split("-")
    price = int(price)
    if item not in inventory[hero]:
        inventory[hero][item] = price

    command = input()

for hero in names:
    print(f"{hero} -> Items: {len(inventory[hero])}, Cost: {sum(inventory[hero].values())}")