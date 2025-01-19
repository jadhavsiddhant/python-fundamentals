# Write a program that counts how many lines are in a file.
filename = '/Users/siddhantsmac/Desktop/120 Questions/Q81.py'

with open(filename, 'r') as file:
    lines = file.readlines()
    line_count = len(lines)

print(f'The file has {line_count} lines.')