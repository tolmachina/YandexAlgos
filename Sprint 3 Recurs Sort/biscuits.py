from typing import List

def inp_data():
    n = int(input())
    kids_size = list(map(int, input().split()))
    m = int(input())
    biscuits_size = list(map(int, input().split()))
    return kids_size,biscuits_size

"""

4 3 1 6

6 3 2 1

6 4 3 1

Get the biggest guy and feed him the biggest cookie 

"""
def greedy_kids(kids_size: List[int], biscuite_size: List[int]) -> int:
    kids_size.sort()
    biscuite_size.sort()
    happy_kids = 0
    while kids_size and biscuite_size:
        biggest_guy = kids_size[-1]
        biggest_biscuit = biscuite_size[-1]

        if biggest_biscuit >= biggest_guy:
            happy_kids += 1
            kids_size.pop()
            biscuite_size.pop()
        else:
            kids_size.pop()
    return happy_kids


kids, biscuits = inp_data()

print(greedy_kids(kids,biscuits))