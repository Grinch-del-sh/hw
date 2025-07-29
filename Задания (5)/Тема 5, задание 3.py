X = 50000  # Minimum investment
A = 60000  # Mike's money
B = 40000  # Ivan's money

both = (A >= X) and (B >= X)
mike_only = (A >= X) and (B < X)
ivan_only = (B >= X) and (A < X)
together = (A + B) >= X and not both

if both:
    print(2)
elif mike_only:
    print("Mike")
elif ivan_only:
    print("Ivan")
elif together:
    print(1)
else:
    print(0)