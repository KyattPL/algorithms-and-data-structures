from random import random


def insertion_sort(arr):
    comparisons = 0
    array_accesses = 0
    for i in range(1, len(arr)):
        array_accesses += 1
        chosenElem = arr[i]
        j = i - 1
        array_accesses += 1
        comparisons += 1
        while j >= 0 and arr[j] > chosenElem:
            array_accesses += 2
            arr[j+1] = arr[j]
            j -= 1
        array_accesses += 1
        arr[j+1] = chosenElem
    print("Insertion sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " + str(array_accesses))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    insertion_sort(array)
