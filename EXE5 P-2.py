import random


numbers = [random.randint(1, 10) for _ in range(20)]
print("Generated list:", numbers)


target = int(input("Enter a number to find its positions: "))


positions = [i for i, num in enumerate(numbers) if num == target]


if positions:
    print(f"The number {target} is found at positions: {positions}")
else:
    print(f"The number {target} is not in the list.")
