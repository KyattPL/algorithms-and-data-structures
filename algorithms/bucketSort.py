from random import randint
from insertionSort import insertion_sort

def bucket_sort(arr, k=5):
    buckets = []
    for i in range(k):
        buckets.append([])
    newTab = []
    maximum = max(arr)
    for i in range(len(arr)):
        index = int(k * arr[i] / maximum)
        if index == k:
            index -= 1
        buckets[index].append(arr[i])
    for i in range(k):
        buckets[i] = insertion_sort(buckets[i])
        for j in range(len(buckets[i])):
            newTab.append(buckets[i][j])
    return newTab


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(randint(0, 9))
    print(bucket_sort(array))