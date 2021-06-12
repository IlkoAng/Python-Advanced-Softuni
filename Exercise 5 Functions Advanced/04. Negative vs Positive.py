def odd_even(num):
    if num > 0:
        return True
    return False


seq = [int(el) for el in input().split()]
positive = []
negative = []

for number in seq:
    if odd_even(number):
        positive.append(number)
    elif not odd_even(number):
        negative.append(number)

print(sum(negative))
print(sum(positive))

negative = [abs(num) for num in negative]


if sum(negative) > sum(positive):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")