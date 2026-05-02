# Accessing Elements

# append() - Adds a single element at the end of the list.
shopping_list = ["milk", "eggs"]
shopping_list.append("bread")
print("After append:", shopping_list)                       # Output: ['milk', 'eggs', 'bread']

# insert() - Adds an element at a specified position.
shopping_list.insert(1, "butter")
print("After insert:", shopping_list)                       # Output: ['milk', 'butter', 'eggs', 'bread']

# extend() - Adds multiple elements from another list (or any iterable) to the end of the list.
shopping_list.extend(["apples", "bananas"])
print("After extend:", shopping_list)                       # Output: ['milk', 'butter', 'eggs', 'bread', 'apples', 'bananas']