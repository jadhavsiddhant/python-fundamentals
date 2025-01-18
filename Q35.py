# Write a function to check if a 3-digit number is an Armstrong number (e.g.,
# 153  1^3 + 5^3 + 3^3 = 153).

number = int(input("Enter a 3-digit number: "))

sum_of_cubes = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10

if number == sum_of_cubes:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")