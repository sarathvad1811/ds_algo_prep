def num_occurances(arr, key):
    firstOcIndex = searchNum(arr, 0, len(arr) - 1, key)
    count = 1
    if firstOcIndex == -1:
        return 0
    # check everything on the left
    left = firstOcIndex - 1
    right = firstOcIndex + 1
    # see how many times it is repeated on the left
    while left >= 0:
        if arr[left] == key:
            count = count + 1
        left = left - 1
    while right < len(arr):
        if arr[right] == key:
            count = count + 1
        right = right + 1
    return count


def searchNum(arr, start, end, key):
    mid = int((start + end) / 2)
    if end < 1:
        return -1
    if arr[mid] == key:
        return mid
    if key < arr[mid]:
        return searchNum(arr, start, mid, key)
    else:
        return searchNum(arr, mid, end, key)


arr = [5, 7, 7, 8, 8, 10]
print(num_occurances(arr, 8))
print(num_occurances(arr, 7))
print(num_occurances(arr, 5))
