#To check whether the year is a leap year or not

def is_leap_year(year):

    # Case A: Divisible by 4 but not divisible by 100
    if year % 4 == 0 and year % 100 !=0:
        return True

    # Case B: Divisible by 400
    if year % 400 == 0:
        return True

sample_years = [2000, 1900, 2024, 2023]

for y in sample_years:
    # Call the function and choose a label based on its Boolean result
    label = "Leap Year" if is_leap_year(y) else "Not a leap year"
    print(f"{y}: {label}")