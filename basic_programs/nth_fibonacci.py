# 0,1,1,2,3,5,8,13,21,....
# using recursion
def nth_fibonacci(n):
    if n < 0:
        return 0

    elif n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


# def nth_fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#         return c


ui = int(input("Enter a number"))
print(nth_fibonacci(ui))
