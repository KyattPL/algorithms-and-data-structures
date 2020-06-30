from algorithms.bubbleSort import bubble_sort
from algorithms.bucketSort import bucket_sort
from algorithms.combSort import comb_sort
from algorithms.countingSort import counting_sort
from algorithms.heapSort import heap_sort
from algorithms.insertionSort import insertion_sort
from algorithms.LSDradixSort import lsd_radix_sort
from algorithms.mergeSort import merge_sort
from algorithms.pigeonholeSort import pigeonhole_sort
from algorithms.quickSort import quick_sort
from algorithms.selectionSort import selection_sort

from random import randint

how_many = 1000
lower_integer = 0
upper_integer = 99

if __name__ == "__main__":
    array = []
    for i in range(how_many):
        array.append(randint(lower_integer, upper_integer))
