# Algorithm: Selection Sort
# Big O Complexity:   
# Best Case Scenario: 
# Worst Case Scenario: 
# Average Case Scenario: 
# Space Complexity: 

# Import the random module
import random

def selection_sort(arr):
    """
    Sort the given array using the selection sort algorithm.
    """
    # Loop through the array
    for i in range(len(arr)):
        # Find the minimum element in the unsorted array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def main():
    # Generate a random array of N elements
    array_size = int(input("Enter the size of the array: "))
    arr = [random.randint(1, 100) for i in range(array_size)]
    print(f"Unsorted array: {arr}")

    # Sort the array and print the result
    selection_sort(arr)
    print(f"Sorted array: {arr}")

if __name__ == "__main__":
    main()