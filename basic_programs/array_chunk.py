# given a list and integer n, generate sub lists of the list each of size n

import math


def chunkify(list, n):
    return_list = []
    num_of_iterations = math.ceil(len(list) / n)

    for j in range(num_of_iterations):
        sub_list = list[j * n : (j + 1) * n]
        if len(sub_list) > 0:
            return_list.append(sub_list)

    return return_list


# def chunkify(list, n):
#     return_list = []
#     j = 0

#     while j < len(list):
#         sub_list = list[j * n : (j + 1) * n]
#         if len(sub_list) > 0:
#             return_list.append(sub_list)
#         j = j + n

#     return return_list

# def chunkify(list, n):
#     return_list = []

#     for num in list:
#         # for every element
#         # if the return list is empty, create a new chunk and insert the element into the chunk
#         if len(return_list) == 0:
#             return_list.append([num])
#             continue

#         last = return_list[-1]
#         # if the size of the list is equal to chunk size then create a new chunk and insert the element into the chunk
#         if len(last) == n:
#             return_list.append([num])
#         else:
#             last.append(num)

#     return return_list


print(chunkify([1, 2, 3, 4], 2))  # [[1, 2], [3, 4]]
print(chunkify([1, 2, 3, 4, 5], 2))  # [[1,2], [3,4], [5]]
print(chunkify([1, 2, 3, 4, 5], 15))  # [[1, 2, 3, 4, 5]]
