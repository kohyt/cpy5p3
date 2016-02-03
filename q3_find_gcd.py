# q3_find_gcd.py
# find greatest common divisor

import numbers
def check():
    if a > 0 and b > 0 and isinstance(a, numbers.Integral) and isinstance(b, numbers.Integral):
        return True
    else:
        return False

def gcd(a,b):
    if a >= b:
        while b != 0:
            d = a % b
            a = b
            b = d
        print(a)
    elif a < b:
        while b != 0:
            d = a % b
            a = b
            b = d
        print(a)

# get input
a = int(input("Enter positive integer:"))
b = int(input("Enter 2nd positive integer:"))

if check():
    gcd(a,b)
else:
    print("Invalid input")

# test
def testrun():
    if gcd(24,16) == 8 and gcd(255,25) == 5:
        return True
    else:
        return False






