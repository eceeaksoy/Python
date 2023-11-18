def tax_calculation(income):
    tax_payable = 0

    if income < 10000:
        tax_payable = 0
    elif income <= 20000:
        tax_payable = (income - 10000) * 10 / 100
    else:
        tax_payable = ((income - 20000) * 20 / 100) + (10000 * 10 / 100)

    return tax_payable

taxable_income = int(input("Enter your income: "))
print("Total tax to pay: ", tax_calculation(taxable_income))