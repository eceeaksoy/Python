def armstrong(num):

    if num == sum([int(i) ** len(str(num)) for i in str(num)]):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")


number = int(input("Enter a number: "))
armstrong(number)