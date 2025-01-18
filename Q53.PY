# Given a list, write a Python function to find all duplicate elements.
def find_duplicates(lst):
    duplicates = []
    seen = set()
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates
lst = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 1]
print(find_duplicates(lst))  