def minNum(arr, start, end):
    mid = int((start + end) / 2)
    # this means the rotation took place at this point
    if arr[mid] > arr[mid + 1]:
        return arr[mid + 1]
    if arr[mid] < arr[mid - 1]:
        return arr[mid]
    if arr[mid] < arr[mid + 1]:
        return minNum(arr, start, mid)
    else:
        return minNum(arr, mid, end)


arr = [3, 4, 5, 1, 2]
# arr = [4,5,1,2,3]
# arr = [5,1,2,3,4]
print(minNum(arr, 0, 5))
