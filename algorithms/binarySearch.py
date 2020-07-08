# Binary search algorithm to find the position of the element
# in a sorted list. (Sorting counts for comparisons)
from random import randint
from quickSort import quick_sort


def binary(lis, elem):
    comparisons = 0
    array_accesses = 0
    (comp1, access1) = quick_sort(lis, 0, len(lis) - 1, 0, 0)
    comparisons += comp1
    access1 += access1
    (result, comparisons, array_accesses) = binary_search(
        lis, 0, len(lis) - 1, elem, comparisons, array_accesses)
    if result != -1:
        print("Binary search:")
        print("Element is present at index: " + str(result))
        print("No. comparisons: " + str(comparisons) +
              ", no. array accesses: " + str(array_accesses))
    else:
        print("Element is not present in array")


def binary_search(arr, l, r, elem, comps, accesses):
    if r >= l:
        mid = l + (r - l) // 2

        comps += 1
        accesses += 1
        if arr[mid] == elem:
            return (mid, comps, accesses)
        elif arr[mid] > elem:
            comps += 1
            accesses += 1
            return binary_search(arr, l, mid-1, elem, comps, accesses)
        else:
            comps += 1
            accesses += 1
            return binary_search(arr, mid + 1, r, elem, comps, accesses)
    else:
        return -1


if __name__ == "__main__":
    lis = []
    for i in range(100):
        lis.append(randint(0, 100))
    binary(lis)
