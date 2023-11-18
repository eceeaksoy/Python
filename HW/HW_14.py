"""
Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.
"""

num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("It is negative number! Factorial does not exist!")
else:
    print(f"The factorial of {num} is", end=" ")
    if num == 0:
        print(1)
    else:
        for i in range(1, num + 1):
            factorial *= i
        print(factorial)