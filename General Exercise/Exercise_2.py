def remove_chars(word, n):
    return word[n:]

str = input("Word: ")
num = int(input("Number: "))
print("New word: " + remove_chars(str,num))