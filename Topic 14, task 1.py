my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_recursive(lst):
    if not lst:  # Base case - empty list
        print("End of list")
        return
    
    print(lst[0])  # Print first element
    print_recursive(lst[1:])  # Recursive call with remaining elements

print_recursive(my_list)