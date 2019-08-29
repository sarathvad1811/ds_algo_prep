def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1

    return True


def print_prime_interval(a, b):
    for i in range(a, b + 1):
        if is_prime(i):
            print(i)


num1 = input("Enter 1st number:")
num2 = input("Enter 2nd number:")
print_prime_interval(int(num1), int(num2))
