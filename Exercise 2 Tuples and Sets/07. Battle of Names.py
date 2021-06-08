n = int(input())
odd_set = set()
even_set = set()
sum_of_el = 0
for num in range(1, n+1):
    name = input()
    sum_of_el = sum([ord(el) for el in name]) // num
    if sum_of_el % 2 == 0:
        even_set.add(sum_of_el)
    else:
        odd_set.add(sum_of_el)

sum_even = sum(even_set)
sum_odd = sum(odd_set)
if sum_even == sum_odd:
    new = [str(el) for el in odd_set.union(even_set)]
    print(", ".join(new))
elif sum_odd > sum_even:
    new = [str(el) for el in odd_set.difference(even_set)]
    print(", ".join(new))
else:
    new = [str(el) for el in odd_set.symmetric_difference(even_set)]
    print(", ".join(new))
