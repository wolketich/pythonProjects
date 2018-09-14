# Algorithm: Bubble Sort

# Import the random module
import random

def sort(arr):
    pass


def main():
    # Generate a random array of N elements
    array_size = int(input("Enter the size of the array: "))
    arr = [random.randint(1, 100) for i in range(array_size)]
    print(f"Unsorted array: {arr}")

    # Sort the array and print the result
    
    print(f"Sorted array: {arr}")

if __name__ == "__main__":
    main()