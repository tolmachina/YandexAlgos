a =int(input()) #base number to calculate hash 
m = int(input()) #module
s = input() #string to hash


# s = s.encode('ascii')
s = list(map(ord, s)) #convert to ascii

def hash(a, m, s):
    i = 1
    member = 0
    hash_num = 0
    for char in s:
        hash_num = (hash_num * a % m + char) % m

    return member % m



def hash_gorner(q, R, s):
    if len(s) == 0:
        return 0

    if len(s) == 1:
        return s[0] % R
    
    if len(s) == 2:
        return (s[0] * q + s[1]) % R

    else:
        member = s[0] * q + s[1]
        for i in range(2, len(s)):
            print(member)
            member = (member * q) % R
            member = (member + s[i]) % R
        return member 

print(hash_gorner(a, m, s))
