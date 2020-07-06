from random import randint


def counting_sort(arr):
    comparisons = len(arr) - 1
    array_accesses = len(arr)
    spread = max(arr) - min(arr) + 1
    additional_space = spread + len(arr)
    countArr = [0] * spread
    newArr = [0] * len(arr)
    for i in range(len(arr)):
        array_accesses += 2
        countArr[arr[i] - min(arr)] += 1
    for i in range(1, spread):
        array_accesses += 2
        countArr[i] += countArr[i-1]
    for i in range(len(arr)-1, -1, -1):
        array_accesses += 4
        countArr[arr[i] - min(arr)] -= 1
        newArr[countArr[arr[i] - min(arr)]] = arr[i]
    print("Counting sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " +
          str(array_accesses) + ", no. additional space required: "
          + str(additional_space))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(randint(0, 10))
    counting_sort(array)
