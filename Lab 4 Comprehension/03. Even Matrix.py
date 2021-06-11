n = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
even_matrix = [[num for num in nums if num % 2 == 0] for nums in matrix]
print(even_matrix)