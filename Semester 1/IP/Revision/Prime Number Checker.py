import math

def is_prime(number):

    # Scenario 1: Handle non-integer inputs (srings, floats)
    try:
        # Reject non-integer floats like 10.5
        if isinstance(number, float) and not number.is_integer():
            return False
        n = int(number)
    except (ValueError, TypeError):
        # Fail on inputs that cannot be converted into int (e.g., "abc")
        return False
    
    # Scenario 2: Handle edge cases based on prime number definition
    # Primes must be greater than 1.
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # Scenario #3: Efficiently check for odd divisors
    # We only need to check for divisors upto the square root of n.
    # We can also skip all even numbers in our check.
    for i in range(3, int(math.sqrt(n)) + 1 ,2):
        if n % i == 0:
            return False
        
    # If no divisors found, the number is prime
    return True

# This block runs only when the script is executed directly
if __name__ == "_main_":
    # A comprehensive list of test cases to validate the function
    test_cases = [
        # --- Standard Cases ---
        17,         # Prime Number
        25,         # Composite Number
        97,         # larger Prime Number
        100,        # Larger Composite Number

        # --- Edge Cases ---
        2,          # Smallest Prime Number
        1,          # Not Prime By Definition
        0,          # Not Prime
        -5,         # Negative Numbers Are Not Prime

        # --- Input Type Cases ---
        "7",        # A String that is a valid prime
        "10",       # A string that is a valid composite Number
        "abc",       # An invalid string
        13.0,       # A float that is a prime integer
        14.0,       # A float that is a composite integer
        13.5,       # A non-integer float
    ]
    print("--- Prime Number Checker: All Scenarios Test ---")
    print("-" * 50)

    # Loop through each test case and print the result
    for case in test_cases:
        if is_prime(case):
            print(f"Input: {case!r:<8} -> Result: PRIME")
        else:
            print(f"Input: {case!r:<8} -> Result: NOT PRIME")
        
    print("-" * 50)