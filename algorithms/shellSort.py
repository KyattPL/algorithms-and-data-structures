from random import random


def shell_sort(arr):
    comparisons = 0
    array_accesses = 0
    additional_space = 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            array_accesses += 1
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                array_accesses += 2
                comparisons += 2
                arr[j] = arr[j-gap]
                j -= gap
            array_accesses += 1
            arr[j] = temp
        gap //= 2

    print("Shell sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " +
          str(array_accesses) + ", no. additional space required: "
          + str(additional_space))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    shell_sort(array)
