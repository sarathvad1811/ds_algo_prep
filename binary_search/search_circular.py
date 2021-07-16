def search_circular(arr, start, end, key):
    mid = (start + end) // 2

    if arr[mid] == key:
        return mid

    if arr[mid] < arr[mid + 1] and arr[mid] < key:
        return search_circular(arr, start, mid - 1)

    elif arr[mid] > arr[mid - 1] and arr[mid] > key:
        return mid - 1

    else:
        return -1


search_circular([9, 10, 2, 5, 6, 8], 2)
