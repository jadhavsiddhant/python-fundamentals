# Write a program that finds the longest word in a text file and prints it.
with open('/Users/siddhantsmac/Desktop/120 Questions/Q83.txt', 'r') as file:
    words = file.read().split()
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

print("The longest word is:", longest_word)