seq = input()
balanced = True
stack = []

for el in seq:
    if el in "[{(":
        stack.append(el)
    elif el in ")}]":
        if len(stack)== 0:
            balanced = False
            break
        opening = stack.pop()

        if f"{opening}{el}" not in ["[]", "{}", "()"]:
            balanced = False
            break

if balanced and len(stack) == 0:
    print("YES")
else:
    print("NO")