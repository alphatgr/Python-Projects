import math

def is_leap(year):
    leap = False
    if year >= 1900 and year <= (math.pow(10, 5)):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
            else:
                leap = True
    return leap

year = int(input())
print(is_leap(year))
