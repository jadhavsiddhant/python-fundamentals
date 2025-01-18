# Given two lists of the same length, create a dictionary mapping elements
# of one list to the corresponding elements of the other.
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

result = {}
for i in range(len(list1)):
    result[list1[i]] = list2[i]

print(result)