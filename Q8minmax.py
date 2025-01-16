# Write a Python program that takes three numbers and prints the largest and the smallest 

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

largest = a if (a > b and a > c) else (b if b > c else c)

smallest = a if (a < b and a < c) else (b if b < c else c)


print("The largest number is:", largest)
print("The smallest number is:", smallest)
