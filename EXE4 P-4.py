def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    square = n ** 2
    return str(square).endswith(str(n))

# Get input from user
num = int(input("Enter a number: "))

# Check and display results
print(f"{num} is Prime" if is_prime(num) else f"{num} is not Prime")
print(f"{num} is Perfect" if is_perfect(num) else f"{num} is not Perfect")
print(f"{num} is Armstrong" if is_armstrong(num) else f"{num} is not Armstrong")
print(f"{num} is Palindrome" if is_palindrome(num) else f"{num} is not Palindrome")
print(f"{num} is Automorphic" if is_automorphic(num) else f"{num} is not Automorphic")
