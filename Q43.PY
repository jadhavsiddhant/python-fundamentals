# Write a program that calculates the sum of all elements in a list.
def sum_of_elements(lst):
    return sum(lst)

example_list = [1, 2, 3, 4, 5]
print("The sum of all elements in the list is:", sum_of_elements(example_list))
# Method 2: Using a for loop
def sum_of_elements_for_loop(lst):
    total = 0
    for element in lst:
        total += element
    return total

print("The sum of all elements in the list using for loop is:", sum_of_elements_for_loop(example_list))