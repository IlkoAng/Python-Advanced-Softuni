def flights(*args):
    mydict = {}
    for idx in range(0, len(args), 2):
        if args[idx].isalpha:
            if args[idx] == "Finish":
                break
            if args[idx] not in mydict:
                mydict[args[idx]] = args[idx+1]
            else:
                mydict[args[idx]] += args[idx+1]
    return mydict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))