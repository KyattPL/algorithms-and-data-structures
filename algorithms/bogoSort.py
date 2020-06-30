# As a joke
from random import randint, random

def bogo_sort(arr):
    while not is_sorted(arr):
        arr = permutation(arr)
    return arr


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True


def permutation(arr):
    indexes = []
    for i in range(len(arr)):
        indexes.append(i)
    newArr = []
    for i in range(len(arr)):
        index = randint(0, len(indexes)-1)
        newArr.append(arr[indexes.pop(index)])
    return newArr

if __name__ == "__main__":
    array = []
    for i in range(10):
        array.append(random())
    bogo_sort(array)
    print("Sorted!")