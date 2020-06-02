# given a string return the most used char and it's count
# eg: aaabbbbccc -> {b: 4}
def max_char(st):
    st = str(st)
    count_map = {}
    max_count = 0
    max_char = ""

    # traverse through the array and get the count of each character
    for c in st:
        if c in count_map:
            count_map[c] = count_map[c] + 1
        else:
            count_map[c] = 1

    # traverse through the hash set to get max count
    for c in count_map:
        if count_map[c] > max_count:
            max_count = count_map[c]
            max_char = c

    return {max_char: max_count}


print(max_char("abbbcccdddbbbcddaaabddbdbcccdedekdjk"))
print(max_char("aaabbbbccc"))
