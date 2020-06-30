from random import random

def comb_sort(arr):
    factor = 1.3
    gap = len(arr)
    isSorted = False
    while not isSorted:
        gap = int(gap / factor)
        if gap <= 1:
            isSorted = True
            factor = 1
        for i in range(len(arr) - gap):
            offsetIndex = gap + i
            if arr[i] > arr[offsetIndex]:
                arr[i], arr[offsetIndex] = arr[offsetIndex], arr[i]
                isSorted = False
    return arr


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    print(comb_sort(array))