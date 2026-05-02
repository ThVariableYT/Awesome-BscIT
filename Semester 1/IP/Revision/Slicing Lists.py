# Slicing Lists
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing: list[start:end:step]
first_five = numbers[0:5]      # Output: [0, 1, 2, 3, 4]
last_three = numbers[-3:]      # Output: [7, 8, 9]
every_second = numbers[::2]    # Output: [0, 2, 4, 6, 8]
reverse_list = numbers[::-1]  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print("First five:", first_five)
print("Every second:", every_second)
print("Reversed:", reverse_list)