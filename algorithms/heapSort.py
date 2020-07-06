from random import random


def heapify(arr, n, i):
    comps = 0
    accesses = 0

    largest = i
    l = 2*i + 1
    r = 2*i + 2

    comps += 2
    accesses += 2
    if l < n and arr[i] < arr[l]:
        largest = l

    comps += 2
    accesses += 2
    if r < n and arr[largest] < arr[r]:
        largest = r

    comps += 1
    if largest != i:
        accesses += 4
        arr[i], arr[largest] = arr[largest], arr[i]
        (comps1, accesses1) = heapify(arr, n, largest)
        comps += comps1
        accesses += accesses1

    return (comps, accesses)


def heap_sort(arr):
    additional_space = 0
    comparisons = 0
    array_accesses = 0

    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        (comparisons1, array_accesses1) = heapify(
            arr, n, i)
        comparisons += comparisons1
        array_accesses += array_accesses1

    for i in range(n-1, 0, -1):
        array_accesses += 4
        arr[i], arr[0] = arr[0], arr[i]
        (comparisons2, array_accesses2) = heapify(
            arr, i, 0)
        comparisons += comparisons2
        array_accesses += array_accesses2

    print("Heap sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " +
          str(array_accesses) + ", no. additional space required: "
          + str(additional_space))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    heap_sort(array)
