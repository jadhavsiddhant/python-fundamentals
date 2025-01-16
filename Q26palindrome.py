# Write a program that checks if a number is a palindrome (e.g., 121 -> palindrome).
number = int(input("Enter a number: "))
original_number = str(number)
reversed_number = original_number[::-1]

if original_number == reversed_number:
    print(number,"is a palindrome number")
else:
    print(number," is not a palindrome number")
