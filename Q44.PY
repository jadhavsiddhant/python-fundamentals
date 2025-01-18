# Write a function that returns the largest and the smallest elements in a
# given list.
def find_largest_and_smallest(lst):
    if not lst:
        return None, None
    largest = max(lst)
    smallest = min(lst)
    return largest, smallest

# Example usage:
numbers = [3, 5, 1, 2, 4, 8]
largest, smallest = find_largest_and_smallest(numbers)
print(f"Largest: {largest}, Smallest: {smallest}")

# Alternate method using a single traversal
def find_largest_and_smallest_single_traversal(lst):
    if not lst:
        return None, None
    largest = smallest = lst[0]
    for num in lst[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

# Example usage:
largest, smallest = find_largest_and_smallest_single_traversal(numbers)
print(f"Largest: {largest}, Smallest: {smallest}")