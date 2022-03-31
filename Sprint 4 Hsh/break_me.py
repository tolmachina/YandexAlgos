import random
import string
from itertools import permutations


A = 1000
R = 123987123

def hash_gorner(s, q=1000, R=123987123):

    s = list(map(ord, s)) #convert to ascii
    if len(s) == 0:
        return 0

    if len(s) == 1:
        return s[0] % R
    
    if len(s) == 2:
        return (s[0] * q + s[1]) % R

    else:
        member = s[0] * q + s[1]

        for i in range(2, len(s)):
            member = (member * q) % R
            member = (member + s[i]) % R
        return member 

s1 = 'ezhgeljkablzwnvuwqvp'
s2 = 'gbpdcvkumyfxillgnqrv'

s1 = list(map(ord, s1))
s2 = list(map(ord, s2))

def brute_search():
    letters = list(string.ascii_lowercase)

    key_word_pairs = {} # hash: word

    for i in range(1,len(letters)):
        library = list(permutations(letters, i))
        for word in library:
            hash = hash_gorner(word)
            if hash not in key_word_pairs:
                key_word_pairs[hash] = (word)
                
            else:
                print(word,key_word_pairs[hash],  hash)
                print(len(key_word_pairs))
                return word,key_word_pairs[hash], hash
        print(hash, key_word_pairs[hash])
    
    return "not found"      
    
print(hash_gorner('ahoes') == hash_gorner('ab'))
brute_search()