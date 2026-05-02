# PRACTICAL NO. 4
# AIM: Convert a Decimal number to Binary number

# Step 1: Get the decimal number from the user and convert to int
decimal = int(input("Step 1: Enter a decimal number: "))
print(f"  You entered: {decimal}\n")

# Step 2: Convert to binary using bin() and remove '0b' prefix
raw_binary = bin(decimal)
binary = raw_binary[2:]
print(f"Step 2: bin({decimal}) returns '{raw_binary}'")
print(f"  After removing prefix: '{binary}'\n")

# Step 3: Display the final binary result
print("Step 3: Final binary representation")
print(f"  Binary: {binary}")