from random import randint


def insertion_sort(arr, comps, accesses):
    for i in range(1, len(arr)):
        accesses += 1
        chosenElem = arr[i]
        j = i - 1
        comps += 1
        accesses += 1
        while j >= 0 and arr[j] > chosenElem:
            comps += 1
            accesses += 1
            arr[j+1] = arr[j]
            j -= 1
        accesses += 1
        arr[j+1] = chosenElem
    return (comps, accesses)


def bucket_sort(arr, k=5):
    comparisons = 0
    array_accesses = 0

    buckets = []
    for i in range(k):
        buckets.append([])
    newTab = []
    maximum = max(arr)
    for i in range(len(arr)):
        array_accesses += 1
        index = int(k * arr[i] / maximum)
        if index == k:
            index -= 1
        buckets[index].append(arr[i])
    for i in range(k):
        (comparisons, array_accesses) = insertion_sort(
            buckets[i], comparisons, array_accesses)
        for j in range(len(buckets[i])):
            newTab.append(buckets[i][j])
    print("Bucket sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " + str(array_accesses))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(randint(0, 9))
    bucket_sort(array)
