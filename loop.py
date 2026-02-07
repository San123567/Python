num = 145
temp = num
total = 0

while temp > 0:
    
    # Extract last digit
    digit = temp % 10  
    fact = 1
    
    # Factorial of digit
    for i in range(1, digit + 1):  
        fact *= i
    total += fact
    
    # Remove last digit
    temp //= 10  

if total == num:
    print(f"{num} is a Special Number")
else:
    print(f"{num} is not a Special Number")
