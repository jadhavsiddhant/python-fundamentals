# Write a function to rotate a list by k positions to the right. For instance,
# [1,2,3,4,5] rotated by 2 becomes [4,5,1,2,3].

def rotate_list(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

rotated_list = rotate_list([1, 2, 3, 4, 5], 2)
print(rotated_list)  