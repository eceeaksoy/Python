def isIsbn(str):
    tot = 0
    j = 10

    for i in str:
        if i == '-':
            tot += 0
        elif i == 'X':
            tot += 10 * j
            j -= 1
        else:
            tot += int(i) * j
            j -= 1

    return True if tot % 11 == 0 else False

print(isIsbn('3-598-21507-X'))
print(isIsbn('3-598-21508-8'))
print(isIsbn('1-234-56789-1'))