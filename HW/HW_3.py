"""
Write a program to create function calculation() such that
it can accept two variables and calculate addition and subtraction.
Also, it must return both addition and subtraction in a single return call.
"""

def calculation(a, b):
    return a+b, a-b

res = calculation(40, 10)
print(res)