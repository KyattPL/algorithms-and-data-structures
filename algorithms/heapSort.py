from random import random


def heapify(arr, n, i, comps, accesses):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    comps += 1
    accesses += 2
    if l < n and arr[i] < arr[l]:
        largest = l

    comps += 1
    accesses += 2
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        accesses += 4
        arr[i], arr[largest] = arr[largest], arr[i]
        (comps, accesses) = heapify(arr, n, largest, comps, accesses)

    return (comps, accesses)


def heap_sort(arr):
    comparisons = 0
    array_accesses = 0

    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        (comparisons, array_accesses) = heapify(
            arr, n, i, comparisons, array_accesses)

    for i in range(n-1, 0, -1):
        array_accesses += 4
        arr[i], arr[0] = arr[0], arr[i]
        (comparisons, array_accesses) = heapify(
            arr, i, 0, comparisons, array_accesses)

    print("Heap sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " + str(array_accesses))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    heap_sort(array)
