x = 36
count = 0

print(f"Finding divisors of {x}:")
for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
        print(f"Found divisor: {i}")
        count += 1
        if i != x // i:
            print(f"Found paired divisor: {x // i}")
            count += 1

print(f"\nTotal number of divisors: {count}")
