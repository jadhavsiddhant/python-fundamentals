import math

# Write a script that uses the math module to compute the square root, floor,
# and ceiling of a user-input number.
number = float(input("Enter a number: "))

sqrt_number = math.sqrt(number)
floor_number = math.floor(number)
ceil_number = math.ceil(number)

print("Square root:", sqrt_number)
print("Floor:", floor_number)
print("Ceiling:", ceil_number)