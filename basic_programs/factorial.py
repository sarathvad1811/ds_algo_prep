# Recursion Approach
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


# Loop Approach
# def factorial(n):
#     fact = 1
#     while n > 1:
#         fact = n * fact
#         n -= 1
#     return fact


print(factorial(5))
