import math

# Function to compute nCr (Combinations)
def nCr(n, r):
    return math.comb(n, r)

# Function to compute nPr (Permutations)
def nPr(n, r):
    return math.perm(n, r)

# Get input values from the user
n = int(input("Enter value for n: "))
r = int(input("Enter value for r: "))

# Compute and display nCr and nPr
print(f"{n}C{r} = {nCr(n, r)}")  # Combinations
print(f"{n}P{r} = {nPr(n, r)}")  # Permutations
