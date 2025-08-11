import math

def generate_factorial_sequence(n):
    """Generates a descending sequence of factorials from n! down to 1!"""
    start_fact = math.factorial(n)
    return [math.factorial(i) for i in range(start_fact, 0, -1)]


print(generate_factorial_sequence(3))