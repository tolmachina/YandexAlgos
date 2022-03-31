

def find_substring(long_str):
    substring = ''
    bst_count = 0
    i = 0
    while i < len(long_str):
        memo = set()
        count = 0
        for ch in range(i, len(long_str)):
            if long_str[ch] not in memo:
                memo.add(long_str[ch])
                # print(memo)
                count += 1
                if count > bst_count:
                    bst_count = count
            else:
                i += 1
                break
        if ch == (len(long_str) - 1):
            break
    return bst_count

long_string = input()
print(find_substring(long_string))
# print(find_substring('peter'))
# print(find_substring('abcabcbb'))
# print(find_substring('bbbbb'))
# print(find_substring('pwwkew'))


# print(find_substring('ojodx'))
# print(find_substring('pwwkew'))
# print(find_substring('pwwkew'))