# Removing Elements

colors = ['red', 'green', 'blue', 'red', 'yellow']

# remove() - Removes the first occurrence of a value.
colors.remove('red')
print("After remove:", colors)                               # Output: ['green', 'blue', 'red', 'yellow']

# pop() - Removes and returns an element at a given position (default is the last).
last_color = colors.pop()                                   # Removes and returns 'yellow'
second_color = colors.pop(1)                                # Removes and returns element at index 1
print("Popped last:", last_color)                           # Output: 'yellow'
print("Popped index:", second_color)                        # Output: 'blue'
print("Remaining colors:", colors)                           # Output: ['green', 'red']

#clear() - Removes all elements from the list.
backup_colors = colors.copy()  # Make a backup first
colors.clear()
print("After clear:", colors)                               # Output: []
print("Backup colors:", backup_colors)                      # Output: ['green', 'red']
