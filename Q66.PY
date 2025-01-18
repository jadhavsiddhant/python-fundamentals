# Given two lists, write a program to find the common elements using sets.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = set(list1) & set(list2)
print(list(common_elements))