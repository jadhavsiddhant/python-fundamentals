# Write a Python program that reads a file and counts the number of words
# in it.
file_path = '/Users/siddhantsmac/Desktop/120 Questions/Q80.py'

file = open(file_path, 'r')
content = file.read()
file.close()

words = content.split()
word_count = len(words)

print("Number of words in the file:", word_count)
