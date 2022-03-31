from typing import List


vector_a = [1, 2, 3, 2, 1]
vector_b = [3, 2, 1, 5, 6]

def common_subarray(vector_a: List[int], vector_b: List[int], n, m):
    max_len = 0
    len_slice = 0
    len_longest = n if n > m else m
    len_smalles = m if m < n else m
    window_size_options = range(len_smalles)
    window_size = window_size_options[len_smalles//2]
    
    while window_size <= len(vector_a):
        memo_a = set()
        memo_b = set()
        for i in range(len(len_longest) + 1 - window_size):
            j = i + window_size
            
            slice_a = tuple(vector_a[i:j])
            if slice_a not in memo_a:
                memo_a.add(slice_a)
            if slice_a in memo_b:
                len_slice = len(slice_a)

            slice_b = tuple(vector_b[i:j])    
            if slice_b not in memo_b:
                memo_b.add(slice_b)
            if slice_b in memo_a:
                len_slice = len(slice_b)
            
            
            if len_slice > max_len:
                max_len = len_slice
                

                # print('max len!', max_len)
        if window_size > m or window_size > n:
            break
        window_size += 1

    # print(memo_a)
    # print(memo_b)
    return max_len


def get_data():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    return a, b, n, m

vector_a, vector_b, n, m = get_data()

print(common_subarray(vector_a, vector_b, n, m))