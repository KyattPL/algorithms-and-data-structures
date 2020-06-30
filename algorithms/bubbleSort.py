from random import random


def bubble_sort(arr):
    comparisons = 0
    array_accesses = 0
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            comparisons += 1
            array_accesses += 2
            if arr[j] > arr[j + 1]:
                array_accesses += 2
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True
        if not swapped:
            break
    print("Bubble sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " + str(array_accesses))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    bubble_sort(array)
