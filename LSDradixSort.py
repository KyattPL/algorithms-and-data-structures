from random import randint

def counting_sort(arr, exp):
    n = len(arr)
    newArr = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i]/exp
        count[index % 10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = n - 1
    while i >= 0:
        index = arr[i]/exp
        newArr[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(len(arr)):
        arr[i] = newArr[i]
    return arr


def lsd_radix_sort(arr):
    maximum = max(arr)
    exp = 1
    while maximum/exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(randint(0,10))
    print(lsd_radix_sort(array))