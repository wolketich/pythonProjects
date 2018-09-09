# Algorithm: Merger Sort

# Import the random module
import random

def merge(left, right):
    """
    Merge two sorted arrays into a single sorted array.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(arr):
    """
    Sort the given array using the merge sort algorithm.
    """
    # Check if the array is empty or contains only one element
    if len(arr) <= 1:
        return arr
    
    # Find the middle of the array
    mid = len(arr) // 2

    # Split the array into two halves
    left = arr[:mid]
    right = arr[mid:]

    # Sort the left half
    left = mergeSort(left)

    # Sort the right half
    right = mergeSort(right)

    # Merge the two halves
    return merge(left, right)


def main():
    # Generate a random array of N elements
    array_size = int(input("Enter the size of the array: "))
    arr = [random.randint(1, 100) for i in range(array_size)]
    print(f"Unsorted array: {arr}")

    # Sort the array and print the result
    sorted_array = mergeSort(arr)
    print(f"Sorted array: {sorted_array}")

if __name__ == "__main__":
    main()