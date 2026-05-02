# Practical NO.5
# AIM: Convert a Decimal number to Hexadecimal

# Step 1: Get input and convert to int
decimal = int(input("Step 1: Enter a decimal number: "))
print(f"  You entered: {decimal}\n")

# Step 2: Convert to hex and remove '0x' prefix
raw_hex = hex(decimal)
hexadecimal = raw_hex[2:].upper()
print(f"Step 2 and 3: hex({decimal}) returns '{raw_hex}', after slicing and uppercase: '{hexadecimal}'\n")

# Step 3: Display the final result
print("Step 4: Final hexadecimal representation")
print(f"  Hexadecimal: {hexadecimal}")
