# A perfect number is a number that is equal to the sum of its positive
# divisors (excluding itself). Write a program to check if a number is perfect.
def is_perfect_number(n):
    sumdivisors = 0
    for i in range(1, n):
        if n % i == 0:
            sumdivisors += i
    return sumdivisors == n

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")