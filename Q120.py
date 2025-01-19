# Write a script that repeatedly asks the user for a number, catches
# ValueError if the input is invalid, and stops when a valid number is entered.
while True:
    try:
        number = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")