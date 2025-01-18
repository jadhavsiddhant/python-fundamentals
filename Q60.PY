# Write a program to check if a given key exists in a dictionary.
def check_key_exists(dictionary, key):
    if key in dictionary:
        print("Key exists in the dictionary.")
    else:
        print("Key does not exist in the dictionary.")

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'
check_key_exists(my_dict, key_to_check)