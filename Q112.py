# Use a lambda function inside map to transform a list of numbers (e.g.,
# multiply each by 2).
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)