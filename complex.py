principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest in %: "))
time = float(input("Enter the time (in years): "))
n= int(input("Enter the number of times"))
amount = principal * (1 + rate/(100 * n))**(n * time)
compound_interest = amount - principal
print("compund interest is:",compound_interest)
print("total interest after",time,"years is:",amount)

