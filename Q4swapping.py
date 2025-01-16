# Write a Python program that swaps the values of two variables without using a temporary 

a , b = map(int , input("Enter two numbers").split())
print("Value of a and b before swapping", a , b)
a = a+b
b = a-b
a = a-b
print("Value of a and b after swapping", a , b)
