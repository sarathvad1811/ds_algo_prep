def num_of_digits(number):
    digits = 0
    while number != 0:
        digits = digits + 1
        number = int(number / 10)

    return digits


def is_amstrong(n):
    temp = n
    digits = num_of_digits(n)

    am_sum = 0
    while n > 0:
        rem = int(n % 10)
        am_sum += rem ** digits
        n = int(n / 10)

    if am_sum == temp:
        return True
    else:
        return False


n = 153
if is_amstrong(n):
    print("It is amstrong")
else:
    print("It is not amstrong")
