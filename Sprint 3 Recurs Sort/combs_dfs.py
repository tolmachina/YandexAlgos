
from typing import List
from collections import deque

alphabet = ["","", "abc", "def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def dfs(digits: str, alphabet: List[str], result: List[str], buffer: str = "") -> None:

    if len(buffer) == len(digits):
        result.append(buffer)
        return
    
    for letter in alphabet[digits[len(buffer)] - '0']:
        dfs(digits, alphabet, result, buffer + letter)

    return None

def combine(digits: str, alphabet: List[str])-> List[str]:
    combinats = []
    dfs(digits, alphabet,combinats)
    return combinats


def combine_bfs(digits,alphabet):
    combinats = deque()
    combinats.append("")
    for i in range(len(digits)):
        while(len(combinats[-1]) == i):
            for letter in alphabet[digits[i]-'0']:
                combinats.append(combinats[-1]+letter)
            combinats.popleft()

print(combine_bfs('232',alphabet))