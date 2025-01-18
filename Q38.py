# Write a program that displays the Collatz sequence for any positive integer
# given by the user.
number = int(input("Enter a positive integer: "))

while number != 1:
    print(number, end=' ')
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1

print(number)