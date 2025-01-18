# Write a program to reverse a list in-place (without using reversed() or
# slicing).
my_list = [1, 2, 3, 4, 5]

left = 0
right = len(my_list) - 1

while left < right:
    my_list[left], my_list[right] = my_list[right], my_list[left]
    left += 1
    right -= 1

print(my_list)