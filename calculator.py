import math


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b
def exp(a,b):
    return a**b

def logarithm(a,base):
    if a<=0:
        raise ValueError("Log undefined for non-positive numbers")
    if base<=0 or base==1:
        raise ValueError("Invalid base")
    return math.log(a,base)

def hypotenuse(a,b):
    return math.sqrt(a**2+b**2)

def square_root(a):
    if a<0:
        raise ValueError("Cannot take sqrt of negative number")
    return math.sqrt(a)


