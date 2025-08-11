numbers = [1, 2, 3, 2, 4, 1, 5]
seen = set()

for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)