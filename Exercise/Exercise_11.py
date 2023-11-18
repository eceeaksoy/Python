from string import ascii_lowercase

def isPangram(str):
    ALPHABET = set(ascii_lowercase)
    return ALPHABET.issubset(str.lower())
"""
    for i in ALPHABET:
        if i not in str2:
            return False
    else:
        return True
"""
print(isPangram("The quick brown fox jumps over the lazy dog."))