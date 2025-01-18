# Write a program that counts the frequency of each element in a list using a
# dictionary.

def count_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency
example_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(count_frequency(example_list))