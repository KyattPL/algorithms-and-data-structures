from random import random


def partition(arr, bottom, top):
    i = bottom - 1
    pivot = arr[top]
    for j in range(bottom, top):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[top] = arr[top], arr[i+1]
    return (i + 1)


def quick_sort(arr, bottom, top):
    if bottom < top:
        pi = partition(arr, bottom, top)
        quick_sort(arr, bottom, pi-1)
        quick_sort(arr, pi+1, top)


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    quick_sort(array, 0, len(array) - 1)
    print(array)
