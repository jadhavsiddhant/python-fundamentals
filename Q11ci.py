# Write a Python program to calculate compound interest given principal, rate, and time in years.
p = float(input("Enter amount:"))
t = int(input("Enter time:"))
r = float(input("Enter ROI:"))

ci = p * pow(1 + r / 100, t)
print("Compund interest on given amount is", (ci-p))