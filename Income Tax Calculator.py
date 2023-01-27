#This program collects data from the user in order to calculate their income tax amount.

grossIncome = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

incomeTax = (grossIncome - 10000 - 3000 * dependents) * 0.2

print(f"The income tax is ${incomeTax}")
