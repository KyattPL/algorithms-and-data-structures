from random import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chosenElem = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chosenElem:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = chosenElem
    return arr


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    print(insertion_sort(array))