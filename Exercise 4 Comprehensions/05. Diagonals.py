n = int(input())
matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]

main = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n-1-r] for r in range(n)]

print(f"First diagonal: {', '.join(str(el)for el in main)}. Sum: {sum(main)}")
print(f"Second diagonal: {', '.join(str(el)for el in secondary)}. Sum: {sum(secondary)}")