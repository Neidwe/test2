import math


def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def remainder_from_division(a, b):
    return a % b

def factorial(a, b):
    return math.factorial(a) * math.factorial(b)

def exponentiation(a, b):
    return a ** b

def root(number):
    if number < 0:
        return -((-number) ** (1 / 2))
    return number ** (1 / 2)
