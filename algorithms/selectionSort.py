from random import random


def selection_sort(arr):
    comparisons = 0
    array_accesses = 0
    additional_space = 0
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr)):
            array_accesses += 1
            comparisons += 1
            if arr[j] < arr[minimum]:
                array_accesses += 1
                minimum = j
        comparisons += 1
        if minimum != i:
            array_accesses += 4
            arr[i], arr[minimum] = arr[minimum], arr[i]
    print("Selection sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " +
          str(array_accesses) + ", no. additional space required: "
          + str(additional_space))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    selection_sort(array)
