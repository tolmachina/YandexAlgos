from typing import List


def inp_data():
    n = input()
    ids = list(map(int, input().split()))
    k_unis = int(input())
    return k_unis,ids

"""
1 1 2 2 3 3 3 4 5 5 5 
k = 2


0 0 0 0 0 0
0 2 2 2 1 3

"""

def conf(k_unis: int, ids: List[int]) -> List[int]:

    count = [0] * (max(ids) + 1)
    for id in ids:
        count[id] += 1

    unis = []
    for i in range(k_unis):
        idx = count.index(max(count))
        unis.append(idx)
        count[idx] = 0

    return unis


def conf_2(k: int, ids: List[int]) -> List[int]:
    count = {}
    for id in ids:
        if id not in count:
            count[id] = 1
        else:
            count[id] += 1

    unis_ids = sorted(count, key=count.get, reverse=True)[:k]
    return unis_ids

k_unis, ids = inp_data()
print(*conf_2(k_unis,ids))
