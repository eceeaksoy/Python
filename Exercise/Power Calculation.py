def exponent(base, exp):
    result = 1
    for i in range(1, exp + 1):
        result *= base
    return result

base = int(input("Enter a base: "))
exp = int(input("Enter an exponent: "))
print(f"{base} raises to the power of {exp}: ", exponent(base, exp))