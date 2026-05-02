# Program 1: Even or Odd
# Read input from the user
num = int(input("Enter an integer: "))          # Convert the user's input to an integer

# Check for zero first
if num == 0:
    print("0 is neither even not odd")          # Handle zero case specially

# If not zero, determine even or odd
elif num % 2 == 0:
    print(f"{num} is even")                     # if remainder is 0, its even
else:
    print(f"{num} is odd")                      # Otherwise its odd