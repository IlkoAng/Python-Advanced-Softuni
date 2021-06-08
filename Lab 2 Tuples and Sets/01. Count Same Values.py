nums = list(map(float, input().split()))
mydict = {}

for num in nums:
    if num not in mydict:
        mydict[num] = 0
    mydict[num] += 1

for key,value in mydict.items():
    print(f"{key} - {value} times")