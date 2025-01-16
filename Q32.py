# Implement the Euclidean algorithm to find the GCD (Greatest Common
# Divisor) of two numbers using a while loop.
a = 56
b = 98

while b:
    a, b = b, a % b

print("The GCD is:", a)