from random import randint


def counting_sort(arr, exp, comps, accesses, space):
    n = len(arr)
    space += n + 10
    newArr = [0] * n
    count = [0] * 10
    for i in range(n):
        accesses += 1
        index = arr[i]//exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n - 1
    while i >= 0:
        accesses += 1
        index = arr[i]//exp
        newArr[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(len(arr)):
        accesses += 1
        arr[i] = newArr[i]
    return (comps, accesses, space)


def lsd_radix_sort(arr):
    comparisons = len(arr) - 1
    array_accesses = len(arr)
    additional_space = 0
    maximum = max(arr)
    exp = 1
    while maximum/exp >= 1:
        (comparisons, array_accesses, additional_space) = counting_sort(
            arr, exp, comparisons, array_accesses, additional_space)
        exp *= 10
    print("LSD Radix sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " +
          str(array_accesses) + ", no. additional space required: "
          + str(additional_space))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(randint(0, 10))
    lsd_radix_sort(array)
