# Write a program that calculates the sum of digits of a given integer.
n = int(input("Enter an integer: "))
s = 0
while n > 0:
    s += n % 10
    n //= 10
print("Sum of digits:", s)