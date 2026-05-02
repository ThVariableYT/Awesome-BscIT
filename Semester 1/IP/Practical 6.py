# Practical 6

# To convert Decimal numbers to Binary numbers

print("Get the decimal number from the user")
decimal_str = input("Enter a Decimal Number")
decimal = int(decimal_str)
print(f"You have entered: {decimal}\n")

print("Convert  to Binary using bin()")
raw_binary = bin(decimal)
print(f"bin({decimal}) returns '{raw_binary}'\n")

print("Remove the '0b' prefix")
binary = raw_binary[2:]
print(f"After slicing: '{binary}'\n")

print("Display the final binary representation")
print("Binary:", binary)