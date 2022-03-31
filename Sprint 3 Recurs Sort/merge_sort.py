from typing import List

from collections import deque
def merge(array, left, mid, right):
    merged_list = []
    lefty = deque(array[left:mid])
    righty = deque(array[mid:right])

    while len(lefty) > 0 or len(righty) > 0:

        if len(lefty) ==  0:
            merged_list.append(righty.popleft())
            
        elif len(righty) == 0:
            merged_list.append(lefty.popleft())
            
        if len(lefty) > 0 and len(righty) > 0:
            if lefty[0] <= righty[0]:
                merged_list.append(lefty.popleft())
            else:
                merged_list.append(righty.popleft())
    array[left:right] = merged_list
    return array

def merge_sort(arr, lf, rg):
    if abs(rg-lf) <= 2:
        if len(arr[lf:rg]) == 1:
            return None
        elif arr[lf]>arr[rg-1]:
            arr[lf],arr[rg-1] = arr[rg-1], arr[lf]   
    else:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merged_arr = merge(arr, lf, mid, rg)

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

num_lines = int(input())
line = list(map(int, input().split()))
# xxx = [-6,-12,-14,14]
# merge_sort(xxx, 0, 4)
# print(xxx)
