# Write a Python program to calculate the sum of the series 1 + 1/2 + 1/3 + …
# + 1/n using a for loop.
n = int(input("Enter the value of n: "))
sum_series = 0

for i in range(1, n + 1):
    sum_series += 1 / i

print("The sum of the series is:", sum_series)