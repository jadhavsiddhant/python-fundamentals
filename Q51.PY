# Write a function to find the second-largest element in a list.
def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second
numbers = [10, 20, 4, 45, 99]
print("Second largest element is:", find_second_largest(numbers))