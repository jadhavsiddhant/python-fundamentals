# Write a program to search for a specific substring in a file and print the
# lines where it appears.
filename = '/Users/siddhantsmac/Desktop/120 Questions/Q84.py'
substring = 'specific substring'

with open(filename, 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    if substring in line:
        print(f'Line {i + 1}: {line.strip()}')