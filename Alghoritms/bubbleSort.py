# Algorithm: Bubble Sort
# Big O Complexity: O(n^2)
# Best Case Scenario: O(n)
# Worst Case Scenario: O(n^2)
# Average Case Scenario: O(n^2)
# Space Complexity: O(1)

# Import the random module
import random

def bubble_sort(arr):
    """
    Sort the given array using the bubble sort algorithm.
    """
    # Loop through the array
    for i in range(len(arr)):
        # Loop through the array again
        for j in range(len(arr)):
            # Swap the elements if the current element is greater than the next element
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def main():
    # Generate a random array of N elements
    array_size = int(input("Enter the size of the array: "))
    arr = [random.randint(1, 100) for i in range(array_size)]
    print(f"Unsorted array: {arr}")

    # Sort the array and print the result
    bubble_sort(arr)
    print(f"Sorted array: {arr}")

if __name__ == "__main__":
    main()