# Difference in indexes exists because for binary search, we
# have to sort the list, therefore changing the order of elements.
from binarySearch import binary, binary_search
from linearSearch import linear_search
from random import shuffle, randint

tab = []
for i in range(1000):
    tab.append(i)
shuffle(tab)
temp = tab[:]

elem = randint(0, 1000)

linear_search(tab, elem)
binary(temp, elem)
