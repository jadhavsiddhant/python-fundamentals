# Write a function that determines whether a number is prime.

n = int(input("Enter number: "))
for i in range(2, n):
    if i%2==0:
        print("Not a prime")
    
print("its a prime number")