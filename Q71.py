# Implement binary search recursively to find an element in a sorted list.
arr = [2, 3, 4, 10, 40]
x = 10

low = 0
high = len(arr) - 1
result = -1

while high >= low:
    mid = (high + low) // 2

    if arr[mid] == x:
        result = mid
        break
    elif arr[mid] > x:
        high = mid - 1
    else:
        low = mid + 1

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")