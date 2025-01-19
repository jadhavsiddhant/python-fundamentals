# Demonstrate advanced list slicing (e.g., reversing a list with slicing,
# skipping elements) in a script.
# Original list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)

skipped_elements_list = my_list[::2]
print("List with every second element:", skipped_elements_list)

skipped_elements_list_3 = my_list[::3]
print("List with every third element:", skipped_elements_list_3)