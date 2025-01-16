# Write a program that calculates the factorial of a given positive integer using a for loop.

n = int(input("Enter the number: "))
result = 1
for i in range (1, n+1):
    result *= i 

print("Factorial of number is:" , result)
