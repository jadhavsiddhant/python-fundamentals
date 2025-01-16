# Write a Python program to round a float to 2 decimal places without 
# using the built-in round() function.

x = float(input("Enter a floating point number"))
f=int(x*100)
print("Round of is:", f/100.0)