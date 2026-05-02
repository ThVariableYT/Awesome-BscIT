# PRACTICAL NO.1
# AIM: Python program to check if a number is even or odd, treating 0 as neither

# Read input from the user
num = int(input("Enter an integer: "))  # convert the user’s input to an integer

# Check for zero first
if num == 0:
    print("0 is neither even nor odd")  # handle zero case specially
elif num % 2 == 0:
    print(f"{num} is even")             # if remainder is 0, it’s even
else:
    print(f"{num} is odd")              # otherwise it’s odd
