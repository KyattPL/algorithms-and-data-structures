from random import random


def comb_sort(arr):
    comparisons = 0
    array_accesses = 0
    additional_space = 0

    factor = 1.3
    gap = len(arr)
    isSorted = False
    while not isSorted:
        gap = int(gap / factor)
        comparisons += 1
        if gap <= 1:
            isSorted = True
            factor = 1
        for i in range(len(arr) - gap):
            offsetIndex = gap + i
            array_accesses += 2
            comparisons += 1
            if arr[i] > arr[offsetIndex]:
                array_accesses += 2
                arr[i], arr[offsetIndex] = arr[offsetIndex], arr[i]
                isSorted = False
    print("Comb sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " +
          str(array_accesses) + ", no. additional space required: "
          + str(additional_space))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    comb_sort(array)
