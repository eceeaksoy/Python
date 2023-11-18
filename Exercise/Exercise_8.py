import random

number = random.randint(1, 9)

guess = int(input("Enter a number between 1 and 9: "))
count = 1
isCorrect = False

while not isCorrect:
    if guess == number:
        result = f'Correct! Number of guess is {count}'
        print(result)
        isCorrect = True
    else:
        guess = int(input("Wrong! Enter another number between 1 and 9: "))
        count += 1