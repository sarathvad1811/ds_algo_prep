def num_reverse(num):
    rev_num = 0
    is_neg = num < 0

    temp = num
    mul = 1
    if is_neg:
        temp = abs(num)
        mul = -1

    while temp != 0:
        rem = int(temp % 10)
        rev_num = (rev_num * 10) + rem
        # print(rem)
        temp = int(temp / 10)

    return mul * rev_num


print(num_reverse(123))
print(num_reverse(-123))
