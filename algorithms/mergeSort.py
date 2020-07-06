from random import random


def merge_sort(arr):
    comparisons = 1
    array_accesses = 0
    additional_space = 0
    if len(arr) > 1:
        array_accesses += len(arr)
        additional_space += len(arr)
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        (comps1, accesses1, space1) = merge_sort(L)
        (comps2, accesses2, space2) = merge_sort(R)
        comparisons += comps1 + comps2
        array_accesses += accesses1 + accesses1
        additional_space += space1 + space2

        i = j = k = 0

        while i < len(L) and j < len(R):
            comparisons += 3
            array_accesses += 4
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        comparisons += 2

        while i < len(L):
            comparisons += 1
            array_accesses += 2
            arr[k] = L[i]
            i += 1
            k += 1
        comparisons += 1

        while j < len(R):
            array_accesses += 2
            arr[k] = R[j]
            j += 1
            k += 1
            comparisons += 1
        comparisons += 1

    return (comparisons, array_accesses, additional_space)


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    (comparisons, array_accesses, additional_space) = merge_sort(array)
    print("Merge sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " +
          str(array_accesses) + ", no. additional space required: "
          + str(additional_space))
