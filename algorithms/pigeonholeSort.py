from random import randint


def pigeonhole_sort(arr):
    comparisons = 2*len(arr) - 2
    array_accesses = len(arr)
    minimum = min(arr)
    size = max(arr) - minimum + 1
    additional_space = size
    holes = [0] * size
    for x in arr:
        array_accesses += 2
        holes[x - minimum] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            comparisons += 1
            holes[count] -= 1
            array_accesses += 1
            arr[i] = count + minimum
            i += 1
        comparisons += 1

    print("Pigeonhole sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " +
          str(array_accesses) + ", no. additional space required: "
          + str(additional_space))


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(randint(0, 10))
    pigeonhole_sort(array)
