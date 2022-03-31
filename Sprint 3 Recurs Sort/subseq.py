t = input()
b = input()

"""
find if template is in seq2, not consequently
abc
ahbgdcu

True - abc is in ahbgdcu.


"""
def subseq2(template: str, seq: str) -> bool:
    i = 0
    for letter in seq:
        if i == len(template):
            return True
        if letter == template[i]:
            i += 1
    return i == len(template)

print(subseq2(t,b))


        