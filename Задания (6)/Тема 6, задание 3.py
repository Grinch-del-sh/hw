# Define the range
A = 3
B = 11

# Generate even numbers using list comprehension
even_numbers = [str(num) for num in range(A, B + 1) if num % 2 == 0]

# Result
print("Even numbers between", A, "and", B, ":", " ".join(even_numbers))
