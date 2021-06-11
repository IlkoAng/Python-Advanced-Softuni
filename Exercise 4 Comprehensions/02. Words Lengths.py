text = input().split(", ")
print(f', '.join([f"{name} -> {len(name)}" for name in text]))