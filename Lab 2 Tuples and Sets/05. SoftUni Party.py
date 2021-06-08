n = int(input())
guests = set()
attended = set()
for _ in range(n):
    name = input()
    guests.add(name)

command = input()
while not command == "END":
    attended.add(command)
    command = input()
unattended = guests - attended

print(len(unattended))
print(f"\n".join(sorted(unattended)))


