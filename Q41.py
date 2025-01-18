# Write a program to count how many times a specific character appears in
# a given string.

string = "hello world"
char = 'o'
count = 0
for c in string:
    if c == char:
        count += 1
print(f"The character '{char}' appears {count} times in the string.")