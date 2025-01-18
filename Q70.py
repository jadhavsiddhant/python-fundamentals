# Write a recursive function that computes the sum of all elements in a list.
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

lst = [1, 2, 3, 4, 5]
print(recursive_sum(lst))