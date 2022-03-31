def hash_gorner(q, R, s):
    
    hasher = []
    if len(s) == 0:
        return hasher.append(0)

    if len(s) == 1:
        hasher.append(0)
        return hasher.append(s[0] % R)
    
    if len(s) == 2:
        hasher.append(0)
        hasher.append(s[0] % R)
        return hasher.append((s[0] * q + s[1]) % R)

    else:
        hasher.append(0)
        hasher.append(s[0] % R)
        member = (s[0] * q + s[1]) % R
        hasher.append(member)
        for i in range(2, len(s)):
            member = (member * q) % R
            member = (member + s[i]) % R
            hasher.append(member)
        return hasher


def hash_array(a,m,s):
    hasher = [0]
    if len(s) == 0:
        return hasher
    if len(s) == 1:
        hasher.append((s[0] * a**(len(s)-1)) % m)
    # if len(s) == 2:
    #     hasher.append((s[0] * a**(len(s)-1)) % m)
    #     hasher.append((s[1] * a**(len(s)-2)) % m)
    else:
        for i in range(1,len(s)):
            hasher.append((s[i - 1] * a**(len(s)-i)) % m)
            
    return hasher

def main():
    s = 'abcdefgh'
    s = list(map(ord, s))
    hashes = hash_array(1000, 1000009, s )
    print(hashes)
    indx = [1,1]
    assert(hashes[indx[0]] == 97 )
    indx = [1,5]
    assert((hashes[indx[1]] - hashes[indx[0] - 1]) == 225076)
    indx = [2,3]
    assert((hashes[indx[1]] - hashes[indx[0]]) == 98099)
    indx = [3,4]
    assert((hashes[indx[1]] - hashes[indx[0] - 1]) == 99100)
    indx = [4,4]
    assert((hashes[indx[1]] - hashes[indx[0] - 1]) == 100)
    indx = [1,8]
    assert((hashes[indx[1]] - hashes[indx[0] - 1]) == 436420)
    indx = [5,8]
    assert((hashes[indx[1]] - hashes[indx[0] - 1]) == 193195)

    a = int(input()) #base number to calculate hash 
    m = int(input()) #module
    s = input() #string to hash
    # s = s.encode('ascii')
    s = list(map(ord, s)) #convert to ascii
    hashes = hash_gorner(a,m,s)
    t = int(input())
    for i in range(t):
        indx = list(map(int,input().split()))
        if indx[0] == indx[1]:
            print(hashes[indx[0]])
        else:
            print((hashes[indx[1]] - hashes[indx[0] - 1]))

if __name__ == '__main__':
    main()