power_dict = {}

for num in range(10, -6, -1):
    power_dict[num] = num ** num

# Display dictionary
print("Resulting dictionary:")
for key, value in power_dict.items():
    print(f"{key}: {value}")