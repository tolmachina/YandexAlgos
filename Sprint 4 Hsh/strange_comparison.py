YES = "YES"
NO = "NO"
"""
mxyskaoghi
qodfrgmslc

YES

agg
xda

NO
"""

def compare(a,b):
    if len(a) != len(b):
        return NO
    library_a = {}
    library_b = {}
    for i in range(len(a)):
        key_a = a[i]
        if key_a not in library_a:
            library_a[key_a] = b[i]
        else:
            if library_a[key_a] != b[i]:
                return NO
        key_b = b[i]
        if key_b not in library_b:
            library_b[key_b] = a[i]
        else:
            if library_b[key_b] != a[i]:
                return NO
    return YES

a = input()
b = input()
print(compare(a, b))

# print(compare("abc", "aaa"))
# print(compare("abc", "xyz"))
# print(compare("agg", "xda"))
# print(compare("mxyskaoghi", "qodfrgmslc"))
# print(compare("agg", "xdd"))
