def compound_interest2(principal, rate, time, n):
    rate = rate / 100  # Convert percentage to decimal
    amount = principal
    
# Loop to apply interest n times per year for given years
    for _ in range(time * n):
        amount += (amount * (rate / n))
    interest = amount - principal
    return amount, interest

# Taking user inputs
P = float(input("Enter Principal: "))
R = float(input("Enter Rate (%): "))
T = int(input("Enter Time (years): "))
n = int(input("Enter Compounds/year: "))

# Calculating interest
total, interest = compound_interest2(P, R, T, n)

# Displaying results
print(f"Total Amount: {total:.2f}")
print(f"Compound Interest: {interest:.2f}")
