# PRACTICAL NO.3:
# AIM: Whether a given year is a Leap Year or Not

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test with sample years
sample_years = [2000, 1900, 2024, 2023]
for y in sample_years:
    print(f"{y}: {'Leap year' if is_leap_year(y) else 'Not a leap year'}")
