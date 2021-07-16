# Find the number of 1’s in a sorted binary array
def num_1s(arr):
    low = 0
    high = len(arr) - 1
    first_found_index = -1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == 1:
            first_found_index = mid
            break

        low = mid + 1

    if first_found_index != -1:
        left = first_found_index
        right = first_found_index + 1
        while left >= 0:
            if arr[left] == 1:
                count = count + 1
            left = left - 1

        while right < len(arr):
            if arr[right] == 1:
                count = count + 1
            right = right + 1

    return count


print(num_1s([0, 0, 0, 0, 0, 0, 1, 1]))
print(num_1s([0, 0, 0, 0, 0]))
print(num_1s([1, 1, 1, 1, 1]))
