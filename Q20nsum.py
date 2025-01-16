# Write a Python program to find the sum of all natural numbers up to a given number n.
sum=0
n = int(input("input the last number: "))
for i in range(1, n+1):
    sum+=i

print("Sum of numbers is", sum)