# Write a recursive function to compute the Greatest Common Divisor (GCD)
# of two numbers
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage
print(gcd(48, 18))  # Output: 6