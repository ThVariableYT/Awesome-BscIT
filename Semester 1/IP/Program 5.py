# Program 5: Hollow Square
n = 5                                           # Side length of the square

for row in range(1, n + 1):
    if row == 1 or row == n:                    # First or last row
        print('* ' * n)

    else:
        # Star, then (n-2) spaces, then star
        print('* ' + '  ' * (n - 2) + '* ')