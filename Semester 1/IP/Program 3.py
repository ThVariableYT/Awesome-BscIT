# Program 3: Centered Pyramid
n = 5                                   # Number of Pyramid Levels

for i in range(1, n + 1):               # Level from 1 upto n
    spaces = ' ' * (n - 1)              # Leading spaces to center the stars
    stars  = '*' * (2 * i - 1)          # Odd number of stars at this level
    print(spaces + stars)               # Combine and print each line