# Generate a dictionary that contains numbers (1 to n) as keys and their
# squares as values.
n = 10
squares = {}
for i in range(1, n + 1):
    squares[i] = i ** 2
print(squares)