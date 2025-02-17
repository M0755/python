import random


odd_integers = [random.randrange(1, 100, 2) for _ in range(5)]  # Generates odd numbers between 1 and 99
print("List of 5 odd integers:", odd_integers)


even_integers = [random.randrange(0, 100, 2) for _ in range(4)] # Generates even numbers between 0 and 98
print("List of 4 even integers:", even_integers)

odd_integers[2] = even_integers
print("List of odd integers after replacement:", odd_integers)



flattened_list = []
for item in odd_integers:
    if isinstance(item, list):
        flattened_list.extend(item)  # Extends the main list with elements of sublist
    else:
        flattened_list.append(item)
print("Flattened list:", flattened_list)


flattened_list.sort()
print("Sorted flattened list:", flattened_list)


