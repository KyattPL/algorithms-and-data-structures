from random import random


def merge_sort(arr):
    comparisons = 0
    array_accesses = 0
    if len(arr) > 1:
        array_accesses += len(arr)
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        (comparisons, array_accesses) = merge_sort(L)
        (comparisons, array_accesses) = merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            comparisons += 1
            array_accesses += 4
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array_accesses += 2
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array_accesses += 2
            arr[k] = R[j]
            j += 1
            k += 1

    return (comparisons, array_accesses)


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    (comparisons, array_accesses) = merge_sort(array)
    print("Merge sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " + str(array_accesses))
