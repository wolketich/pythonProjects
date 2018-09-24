import random

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
#Random array
arr = [1, 3, 5, 7, 9, 11, 13, 15]


# Target element (random item from the array)
random_index = random.randint(0, len(arr) - 1)
target = arr[random_index]

print('Array:', arr)
print('Target element:', target)


print('Index of the target element:', linear_search(arr, target))
