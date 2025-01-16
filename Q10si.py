# Write a Python program that calculates simple interest. Prompt for principal, rate, 
# and time, then compute the interest.

p = float(input("Enter amount:"))
t = float(input("Enter time:"))
r = float(input("Enter ROI:"))
si = (p*t*r)/100
print("Simple interest on given amount is", si)