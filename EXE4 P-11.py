import math

# Function to calculate sin(x) using the series expansion
def sin_series(x, terms=10):
    sin_x = 0
    for n in range(terms):
        # Alternate sign for each term
        sign = (-1) ** n
        # Using the series formula: (-1)^n * x^(2n+1) / (2n+1)!
        sin_x += sign * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return sin_x

# Get input from the user
x = float(input("Enter the value of x in radians: "))

# Calculate sin(x) using the series
result = sin_series(x)
print(f"sin({x}) ≈ {result}")
