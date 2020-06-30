from bubbleSort import bubble_sort
from bucketSort import bucket_sort
from combSort import comb_sort
from countingSort import counting_sort
from heapSort import heap_sort
from insertionSort import insertion_sort
from LSDradixSort import lsd_radix_sort
from mergeSort import merge_sort
from pigeonholeSort import pigeonhole_sort
from quickSort import quick_sort
from selectionSort import selection_sort

from random import randint

how_many = 1000
lower_integer = 0
upper_integer = 99

if __name__ == "__main__":
    array = []
    for i in range(how_many):
        array.append(randint(lower_integer, upper_integer))
    temp = array[:]
    bubble_sort(temp)
    temp = array[:]
    bucket_sort(temp)
    temp = array[:]
    comb_sort(temp)
    temp = array[:]
    counting_sort(temp)
    temp = array[:]
    heap_sort(temp)
    temp = array[:]
    insertion_sort(temp)
    temp = array[:]
    lsd_radix_sort(temp)
    temp = array[:]
    pigeonhole_sort(temp)
    temp = array[:]
    selection_sort(temp)
    temp = array[:]
    (comparisons, array_accesses) = merge_sort(temp)
    print("Merge sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " + str(array_accesses))
    temp = array[:]
    (comparisons, array_accesses) = quick_sort(temp, 0, len(temp) - 1, 0, 0)
    print("Quick sort:")
    print("No. comparisons: " + str(comparisons) +
          ", no. array accesses: " + str(array_accesses))
