# Write a simple “guess the number” game. The program randomly generates a number between 
# 1 and 10, and the user has to guess it.
import random
number = random.randint(1, 10)
guess = int(input("Guess the number (between 1 and 10): "))
if guess == number:
    print("Congratulations! You guessed correctly.")
else:
    print(f"Wrong guess! The correct number was.", number)