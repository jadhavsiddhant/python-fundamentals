from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))
sum_of_filtered_numbers = reduce(lambda x, y: x + y, filtered_numbers)
print(sum_of_filtered_numbers)
