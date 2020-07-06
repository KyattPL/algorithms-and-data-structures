from random import random


def partition(arr, bottom, top, comps, accesses):
    accesses += 1
    i = bottom - 1
    pivot = arr[top]
    for j in range(bottom, top):
        accesses += 1
        comps += 1
        if arr[j] < pivot:
            i += 1
            accesses += 3
            arr[i], arr[j] = arr[j], arr[i]

    accesses += 3
    arr[i+1], arr[top] = pivot, arr[i+1]
    return (i + 1, comps, accesses)


def quick_sort(arr, bottom, top, comps, accesses):
    if bottom < top:
        (pi, comps1, accesses1) = partition(arr, bottom, top, comps, accesses)
        (comps2, accesses2) = quick_sort(arr, bottom, pi-1, comps, accesses)
        (comps3, accesses3) = quick_sort(arr, pi+1, top, comps, accesses)
        (comps, accesses) = (comps1 + comps2 +
                             comps3, accesses1 + accesses2 + accesses3)
    return (comps, accesses)


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    (comparisons, array_accesses) = quick_sort(
        array, 0, len(array) - 1, 0, 0)
    additional_space = 0
    print("Quick sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " +
          str(array_accesses) + ", no. additional space required: "
          + str(additional_space))
