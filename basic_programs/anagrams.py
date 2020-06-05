# given two string A and B, return if they are anagrams or not


# character map solution
def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    count_1 = {}
    for c in str1:
        if c in count_1:
            count_1[c] = count_1[c] + 1
        else:
            count_1[c] = 1

    count_2 = {}
    for c in str2:
        if c in count_2:
            count_2[c] = count_2[c] + 1
        else:
            count_2[c] = 1

    for ch in str1:
        if (ch in count_2) and (count_1[ch] != count_2[ch]):
            return False

    return True


# sort the characters of the string and check if the sorted strings are same or not
# def is_anagram(str1, str2):
#     s1 = "".join(sorted(str1))
#     s2 = "".join(sorted(str2))

#     if s1 == s2:
#         return True

#     return False


print(is_anagram("silent", "listen"))
print(is_anagram("bad", "dad"))
