def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.
    If the target value is not in the array, return -1.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test case
#Random array
arr = [1, 3, 5, 7, 9, 11, 13, 15]

target = 11

print('Array:', arr)
print('Target element:', target)