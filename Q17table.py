# Write a program to display the multiplication table of a given integer up to 10.

x = int(input("Enter the number: "))
for i in range(1,11):
    print(x,"x",i,'=',x*i)