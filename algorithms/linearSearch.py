# Linear search algorithm to find the position of the element
# in an unsorted list
from random import randint


def linear_search(arr, elem):
    comparisons = 0
    array_accesses = 0
    for (index, i) in enumerate(arr):
        array_accesses += 1
        comparisons += 1
        if i == elem:
            break
    print("Linear search:")
    print("Element is present at the index: " + str(index))
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " + str(array_accesses))


if __name__ == "__main__":
    lis = set()
    for i in range(100):
        lis.add(randint(0, 100))
    linear_search(lis, randint(0, 100))
