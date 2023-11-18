"""
Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.
"""

num = int(input("Enter a number: "))
digit = 0

while num != 0:
    num = num // 10
    digit += 1

print("Total digits of this number:", digit)