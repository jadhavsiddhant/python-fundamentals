# Write a Python program that determines if a given number is even or odd.

x = int(input("Enter a number:"))
if x % 2==0:
    print("Entered number is even")
elif x <= 0:
    print("Number is zero or negetive")
else:
    print("Entered number is odd")