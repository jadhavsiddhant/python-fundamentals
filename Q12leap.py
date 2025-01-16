# Write a program that checks if a given year is a leap year.

year = int(input("Enter the year: "))
if year%4==0:
    print("It's a leap year")
else:
    print("Not a leap year")