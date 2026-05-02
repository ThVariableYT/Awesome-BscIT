# Decimal to Binary

# Step 1: Read input from user
print("Step 1: Get the decimal number from the user.")
decimal_str = input("Enter a decimal number: ")
decimal = int(decimal_str)                                          # Convert the decimal string into a integer
print(f" You entered: {decimal}\n")

#Step 2: Python's built-in conversion
print("Step 2: Convert to binary using bin()")
raw_binary = bin(decimal)                                           # Raw binary is a string like '0b1010'
print(f"  bin({decimal}) returns '{raw_binary}'\n")

# Step 3: Remove the '0b' prefix
print("Step 3: Remove the '0b' prefix")
binary = raw_binary[2:]                                             # Slice off the first two characters
print(f" After slicing: '{binary}'\n")

# Step 4: Show the final result
print("Step 4: Show the final binary representation")
print(" Binary:", binary)