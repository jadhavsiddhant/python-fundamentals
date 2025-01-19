# Write a program that appends a user-input line to an existing file without
# overwriting it.
file_path = '/Users/siddhantsmac/Desktop/120 Questions/Q85.py'
user_input = input("Enter a line to append to the file: ")
with open(file_path, 'a') as file:
    file.write(user_input + '\n')