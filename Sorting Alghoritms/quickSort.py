# Algorithm: Quick Sort

# Import the random module
import random

def quickSort(arr):
    """
    Sort the given array using the quick sort algorithm.
    """
    # If the array is empty or contains only one element, return the array
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot element
    pivot = arr[random.randint(0, len(arr) - 1)]

    # Partition the array into two subarrays
    left, right = [], []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    # Sort the subarrays
    left = quickSort(left)
    right = quickSort(right)

    # Return the sorted array
    return left + right


def main():
    # Generate a random array of N elements
    array_size = int(input("Enter the size of the array: "))
    arr = [random.randint(1, 100) for i in range(array_size)]
    print(f"Unsorted array: {arr}")

    # Sort the array and print the result
    quickSort(arr)
    print(f"Sorted array: {arr}")

if __name__ == "__main__":
    main()