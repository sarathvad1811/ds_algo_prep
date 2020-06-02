def reverse(str):
    if len(str) == 0:
        return str

    return reverse(str[1:]) + str[0]


def str_palindrome(str):
    # rev_str = reverse(str)
    str_len = len(str)
    for i in range(str_len):
        # if str[i] != str[len - i - 1]:
        #     return False
        print(i)

    return True


print(str_palindrome("abba"))
print(str_palindrome("baqqqab"))
# print(reverse("hello"))
