n = int(input())
mylist = []

for num in range(n):
    command = input().split()
    if command[0] == "1":
        mylist.append(int(command[1]))

    elif command[0] == "2":
        if mylist:
            mylist.pop()
        else:
            continue

    elif command[0] == "3":
        print(max(mylist))

    elif command[0] == "4":
        print(min(mylist))

mylist = mylist[::-1]
mylist = [str(num) for num in mylist]
print(", ".join(mylist))