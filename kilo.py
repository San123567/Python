import cmath

# Taking input for coefficients
a = float(input("Enter coefficient a: "))  # Coefficient of x^2
b = float(input("Enter coefficient b: "))  # Coefficient of x
c = float(input("Enter coefficient c: "))  # Constant term

# Calculating discriminant
d = cmath.sqrt(b**2 - 4*a*c)  # Using cmath.sqrt to handle negative discriminant

# Finding roots using quadratic formula
root1 = (-b + d) / (2*a)
root2 = (-b - d) / (2*a)

# Displaying the roots
print("Root 1 is:", root1)
print("Root 2 is:", root2)
