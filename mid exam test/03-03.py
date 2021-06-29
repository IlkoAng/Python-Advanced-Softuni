def stock_availability(*args):
    new = args[0]
    if args[1] == "delivery":
        for idx in range(2, len(args)):
            new.append(args[idx])
    elif args[1] == "sell":
        if len(args) > 2:
            for idx in range(2, len(args)):
                if isinstance(args[idx], int):
                    for _ in range(args[idx]):
                        new.pop(0)
                else:
                    res = []
                    [res.append(x) for x in new if x not in res]
                    for idx_2 in range(2, len(args)):
                        if args[idx_2] in res:
                            res.remove(args[idx_2])
                            return res
        if len(args) == 2:
            new.pop(0)
    return new


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
