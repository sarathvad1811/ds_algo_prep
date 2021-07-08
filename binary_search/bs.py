def bs_rec(arr, start, end, key):
    if end < start:
        return -1

    mid = int((start + end) / 2)

    if arr[mid] == key:
        return mid

    if key > arr[mid]:
        return bs_rec(arr, mid + 1, end, key)
    else:
        return bs_rec(arr, start, mid - 1, key)


arr = [1, 2, 3, 4, 5]

print(bs_rec(arr, 0, len(arr) - 1, 5))
print(bs_rec(arr, 0, len(arr) - 1, 65))

