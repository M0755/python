def print_reverse_natural_numbers(n):
    for num in range(n, 0, -1):
        print(num, end=" ")


n = int(input("Enter a number N: "))


print_reverse_natural_numbers(n)
