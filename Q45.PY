# Write a Python function that removes duplicate elements from a list and
# returns the new list.
def remove_duplicates(input_list):
    return list(set(input_list))

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5]
new_list = remove_duplicates(original_list)
print(new_list)  # Output: [1, 2, 3, 4, 5]