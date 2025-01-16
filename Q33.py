# Write a Python function to compute the LCM (Least Common Multiple) of
# two numbers, leveraging the GCD.
import math
def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

# Example usage:
num1 = 12
num2 = 15
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")