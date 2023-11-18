str = input("Enter a word: ")
mid = int(len(str)/2)
newWord = str[0] + str[mid] + str[-1]
print(newWord)