#import matplotlib
# Simple Calculator - Version 3
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(base, exponent):
    return base ** exponent

# Test all functions
print("1 + 2 =", add(1, 2))
print("5 - 3 =", subtract(5, 3))
print("2 * 3 =", multiply(2, 3))
print("10 / 2 =", divide(10, 2))
print("2^3 =", power(2, 3))