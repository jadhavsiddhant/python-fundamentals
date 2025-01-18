# Write a Python program that counts the number of times a given element
# appears in a list.

my_list = [1, 2, 3, 4, 2, 2, 5, 2, 6, 7, 8, 2]

element = 2

count = 0

for item in my_list:
    if item == element:
        count += 1

print(f"The element {element} appears {count} times in the list.")