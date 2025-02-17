def find_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  # Start from 'a' to avoid duplicates
            c = (a**2 + b**2) ** 0.5  # Compute 'c'
            if c.is_integer() and c <= limit:  # Check if 'c' is an integer
                triplets.append((a, b, int(c)))
    return triplets

# Generate triplets with side length ≤ 30
limit = 30
triplets = find_pythagorean_triplets(limit)

# Display the triplets
print("Pythagorean Triplets with side length ≤ 30:")
for triplet in triplets:
    print(triplet)
