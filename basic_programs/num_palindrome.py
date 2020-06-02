def is_palindrome(num):
    rev_num = 0

    temp = num
    mul = 1
    if num < 0:
        mul = -1
        temp = abs(num)

    while temp != 0:
        rem = int(temp % 10)
        rev_num = (rev_num * 10) + rem
        temp = int(temp / 10)

    rev_num = rev_num * mul

    print(rev_num)

    return num == rev_num


print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(100))
print(is_palindrome(0))
