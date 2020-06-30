from random import random

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        if minimum != i:
            arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(random())
    print(selection_sort(array))