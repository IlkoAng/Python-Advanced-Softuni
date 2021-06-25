import re

file = open("text.txt")

for idx, line in enumerate(file.readlines()):
    if idx % 2 != 0:
        continue

    line = re.sub('[-,.!?]', '@', line)
    line = ' '.join(reversed(line.split()))

    print(line.strip())


