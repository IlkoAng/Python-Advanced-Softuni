num = int(input())
mydict = {}

for _ in range(num):
    token = input().split()
    name = token[0]
    grade = float(token[1])

    if name not in mydict:
        mydict[name] = []
    mydict[name].append(grade)

for key, value in mydict.items():
    mark_str = list(map(lambda f: format(f, '.2f'), value))
    print(f"{key} -> {' '.join(mark_str)} (avg: {sum(value) / len(value):.2f})")