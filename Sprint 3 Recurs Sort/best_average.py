from collections import deque
from curses import halfdelay

"""
0 0 0 1 3 3 5 10
4 4 5 7 7 7 8 9 9 10

0 0 0 1 3 3 4 4 5 5 7 7 7 8 9 9 10 10
1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 17 18
"""
n = input()
m = input()
north = list(map(int, input().split()))
south = list(map(int, input().split()))

def get_median(north,south):
    i, j = 0, 0
    sum_len  =len(north) + len(south)
    median = sum_len // 2
    odd = False
    if sum_len % 2 == 0:
        odd = True
    half_median = median // 2
    i,j = half_median, half_median
    while True:
        if north[i] < south[j]:
            median -= half_median
            i += median // 2

        elif south[i] < north[j]:
            median -= half_median
            j += median // 2
        else:
            print("equal")
            median -= half_median
            i += median // 2
        if median <= 1:
            if not odd:
                return min(south[j], north[i])
            else:
                if south[j] == north[i]:
                    return south[j]
                else:
                    return (south[j] + north[i]) / 2
                

print(get_median(north, south))