# Algorithm: Quick Sort

# Import the random module
import random

def quickSort(arr):
    """
    Sort the given array using the quick sort algorithm.
    """
    # If the length of the array is less than 1, return the array
    if len(arr) < 1:
        return arr

    # Get the pivot element
    pivot = arr[len(arr) // 2]

    # Get the elements less than the pivot
    left = [x for x in arr if x < pivot]

    # Get the elements equal to the pivot
    middle = [x for x in arr if x == pivot]

    # Get the elements greater than the pivot
    right = [x for x in arr if x > pivot]

    # Return the sorted array
    return quickSort(left) + middle + quickSort(right)


def main():
    # Generate a random array of N elements
    array_size = int(input("Enter the size of the array: "))
    arr = [random.randint(1, 100) for i in range(array_size)]
    print(f"Unsorted array: {arr}")

    # Sort the array and print the result
    sorted_arr = quickSort(arr)
    print(f"Sorted array: {sorted_arr}")

if __name__ == "__main__":
    main()