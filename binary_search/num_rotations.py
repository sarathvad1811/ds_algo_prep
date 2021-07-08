# find the number of arrays in a circularly sorted array
# [4,5,1,2,3] -> 2
# [5,1,2,3,4] -> 1
# [1,2,3,4,5] -> 0
def num_rotations(arr):
    # 1 -> find the min index of the array
    (start, end) = (0, len(arr) - 1)
    if arr[start] < arr[end]:
        # already sorted array
        return start

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > arr[mid + 1]:
            # rotation took at this place
            return mid + 1
        elif arr[mid] < arr[mid - 1]:
            return mid
        else:
            # update start or end
            if arr[mid] > arr[end]:
                start = mid + 1
            else:
                end = mid - 1


print(num_rotations([1, 2, 3, 4, 5]))
print(num_rotations([2, 3, 4, 5, 1]))
print(num_rotations([4, 5, 1, 2, 3]))
print(num_rotations([5, 1, 2, 3, 4]))

