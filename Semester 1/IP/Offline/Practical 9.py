#PRACTICAL NO.9
# AIM: Display a Factorial of a given number

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i)
    return result


# Printing till Factorial of 11:

print("Factorial of 0 is",factorial(0))
print("Factorial of 1 is",factorial(1))
print("Factorial of 2 is",factorial(2))
print("Factorial of 3 is",factorial(3))