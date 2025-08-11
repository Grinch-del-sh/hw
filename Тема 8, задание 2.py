N = 5  # Predefined N
arr = [1, 2, 3, 4, 5]  # Predefined array

# Reorder and print
new_arr = [arr[-1]] + [arr[i//2] if i%2==0 else arr[-2 - i//2] for i in range(1, N)]
print(*new_arr)