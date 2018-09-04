# Algorithm: Insertion Sort

# Import the random module
import random

def insertion_sort(arr):
    """
    Sort the given array using the insertion sort algorithm.
    """
    # Loop through the array
    for i in range(1, len(arr)):
        # Get the current element
        current = arr[i]
        # Get the previous element
        j = i - 1
        # Compare the current element with the previous elements
        while j >= 0 and current < arr[j]:
            # Swap the elements if the current element is smaller than the previous element
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def main():
    # Generate a random array of N elements
    array_size = int(input("Enter the size of the array: "))
    arr = [random.randint(1, 100) for i in range(array_size)]
    print(f"Unsorted array: {arr}")

    # Sort the array and print the result
    insertion_sort(arr)
    print(f"Sorted array: {arr}")

if __name__ == "__main__":
    main()