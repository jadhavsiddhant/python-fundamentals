# Write a Python program to convert a temperature from Celsius to Fahrenheit and vice versa.
print("1. Celsisu to fahrenheit\n2. fahrenhiest to celsius")
choice = int(input("Enter your choice"))
if choice==1:
    c = int(input("Enter temprature in celsius: "))
    f = (c * 9/5)+32
    print(c, "celsius in fahrenheit is", f)
elif choice==2:
    f = float(input("Enter temperature in fahrenheit: "))
    c = (f-32)*(5/9)
    print(f, "fahrenheit in celsius is", c)
else:
    print("Enter 1 or 2")