# 0,1,1,2,3,5,8,13,21,....
# using recursion
def print_fibonacci(n):
    print("0")
    print("1")
    a = 0
    b = 1
    for i in range(1, n + 1):
        c = a + b
        a = b
        b = c
        print(c)


user_input = input("Enter a number:")
print_fibonacci(int(user_input))
