def divisible(number):
    divisible = [num for num in range(2,11) if number % num == 0]
    return True if divisible else False


start = int(input())
stop = int(input())

print([num for num in range(start, stop+1) if divisible(num)])




