# Write a function to merge two dictionaries. If a key appears in both, add
# their values.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Add values if key exists in both dictionaries
        else:
            merged_dict[key] = value  # Add the key-value pair if key is not in the first dictionary
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
result = merge_dictionaries(dict1, dict2)
print(result)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}