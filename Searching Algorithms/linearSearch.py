def linear_search(arr, target):
    """
    Searches for the target element in the given array using linear search algorithm.
    Returns the index of the target element if found, else returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test case
arr = [1, 2, 3, 4, 5]
target = 3

print('Index of the target element:', linear_search(arr, target))
