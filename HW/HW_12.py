"""
Print the following pattern
Write a program to use for loop to print the following reverse number pattern
"""

row = 5

for i in range(0, row + 1):
    for j in range(row - i, 0, -1):
        print(j, end=" ")
    print()