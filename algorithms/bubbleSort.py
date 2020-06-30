from random import random

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    bubble_sort(array)
    print(bubble_sort(array))