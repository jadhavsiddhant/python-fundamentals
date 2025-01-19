import statistics

# Use the statistics module to compute the mean, median, and mode of a list
# of numbers.
data = [1, 2, 2, 3, 4, 4, 4, 5, 6]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")