# Practical 4

# Write a program to convert a character digit to an integer

def char_to_int(c):
    return int(c)

# UseCase 1: Single character from user
ch = input("Enter a digit (0-9): ")
print("Converted integer is", char_to_int(ch))

# UseCase 2: All digits in a string 
s = "314159"
nums = [char_to_int(c) for c in s]
print("List of integers is", nums)