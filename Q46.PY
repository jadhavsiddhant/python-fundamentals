# Implement a linear search to find a given element in a list. Return the index
# if found, or -1 otherwise.

my_list = [1, 2, 3, 4, 5]
target = 3
index = -1

for i in range(len(my_list)):
    if my_list[i] == target:
        index = i
        break

print("Element found at index:", index)