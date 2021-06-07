expression = input()
mylist = []

for idx in range(len(expression)):
    if expression[idx] == "(":
        mylist.append(idx)
    elif expression[idx] == ")":
        start = mylist.pop()
        print(expression[start:idx+1])