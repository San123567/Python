# The following code solves a quadratic equation using Dharacharya's Formula

def solve_quadratic_equation(a,b,c):
  # Calculating discriminant
  discriminant = b**2 - 4*a*c
  roots = [0,0]
  roots[0] = (-b + discriminant**0.5)/(2*a)
  roots[1] = (-b - discriminant**0.5)/(2*a)
  return roots

# Taking user input for coefficients and constant
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Calling the Function
if a>0:
  roots = solve_quadratic_equation(a,b,c)
  print("The roots of the equation are: ",roots)
else:
  print("a should be greater than 0")
