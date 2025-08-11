m = 150  # Max boat weight
n = 4  # Number of fishermen
weights = [80, 60, 70, 50]  # Individual weights

weights.sort()
left = 0
right = n - 1
boats = 0

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1
    right -= 1
    boats += 1

print(boats)