# Algorithm: Heap Sort

# Import the random module
import random

def heapSort(arr):
    """
    Sort the given array using the heap sort algorithm.
    """
    # Build a max heap
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)
    
    # Extract elements from the heap
    for i in range(len(arr) - 1, 0, -1):
        # Swap the first element with the last element
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify the root element
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    """
    Heapify the given array.
    """
    # Initialize the largest element as the root
    largest = i
    # Get the left child
    left = 2 * i + 1
    # Get the right child
    right = 2 * i + 2

    # If the left child is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # If the right child is greater than the root
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If the largest element is not the root
    if largest != i:
        # Swap the elements
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root
        heapify(arr, n, largest)


def main():
    # Generate a random array of N elements
    array_size = int(input("Enter the size of the array: "))
    arr = [random.randint(1, 100) for i in range(array_size)]
    print(f"Unsorted array: {arr}")

    # Sort the array and print the result
    sorted_arr = heapSort(arr)
    print(f"Sorted array: {sorted_arr}")
    

if __name__ == "__main__":
    main()