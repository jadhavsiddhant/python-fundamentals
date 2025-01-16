# Write a program to count the number of words in a user-input string
# (words are separated by spaces).


user_input = input("Enter a string: ")
words = user_input.split()
word_count = len(words)
print("Number of words:", word_count)