# Program 4: Diamond Shape
n = 5                                   # Half-Height of the diamond (middle row)

# Top half (including middle)
for i in range(1, n + 1):
    spaces = ' ' * (n - i)              # Leading spaces
    stars  = '*' * (2 * i - 1)          # Increasing stars
    print(spaces + stars)               # Print one line

# Bottom half (Excluding middle)
for i in range(n - 1, 0, -1):
    spaces = ' ' * (n - i)              # Leading spaces
    stars  = '*' * (2 * i - 1)          # Increasing stars
    print(spaces + stars)               # Print one line