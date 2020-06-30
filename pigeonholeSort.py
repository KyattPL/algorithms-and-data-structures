from random import randint

def pigeonhole_sort(arr):
    minimum = min(arr)
    size = max(arr) - minimum + 1
    holes = [0] * size
    for x in arr:
        holes[x - minimum] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + minimum
            i += 1
    return arr

if __name__ == "__main__":
    array = []
    for i in range(20):
        array.append(randint(0, 10))
    print(pigeonhole_sort(array))