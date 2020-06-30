from random import randint

def counting_sort(arr):
    spread = max(arr) - min(arr) + 1
    countArr = [0] * spread
    newArr = [0] * len(arr)
    for i in range(len(arr)):
        countArr[arr[i]] += 1
    for i in range(1, spread):
        countArr[i] += countArr[i-1]
    for i in range(len(arr)-1, -1, -1):
        countArr[arr[i]] -= 1
        newArr[countArr[arr[i]]] = arr[i]
    return newArr


if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(randint(0,10))
    print(counting_sort(array))