

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
                merge_segments
                merged_list.append(lefty.popleft())
            else:
                merged_list.append(righty.popleft())
    array[left:right] = merged_list
    return array


def merge_segments(a,b):
    # (7,8) == (7,8)
    if a[0] == b[0] and a[1] == b[1]:
        return a
    # (6,10) > (7,8) || (7,10) > (7,8)
    elif a[0] <= b[0] and a[0] >= b[1]:
        return a
    # (7,8) < (6,10)
    elif b[0] <= a[0] and b[1] >= a[1]:
        return b
    # (2,4) (3,5)
    elif a[0]<b[0] and (b[1]>=a[1]>=b[0]):
        return [a[0],b[1]]
    # (2,4) (3,5)
    elif b[0]<a[0] and (a[1]>=b[1]>=a[0]):
        return [b[0],a[1]]    
    else:
        None

def gardening(arr, lf, rg):
    if abs(rg-lf) <= 2:
        if len(arr[lf:rg]) == 1:
            return None
        elif arr[lf][0]>arr[rg-1][0]:
            arr[lf],arr[rg-1] = arr[rg-1], arr[lf]
    else:
        mid = (lf + rg) // 2
        gardening(arr, lf, mid)
        gardening(arr, mid, rg)
        merged_arr = merge(arr, lf, mid, rg)
    
    return merged_arr



def test_gardening():
    print(
    gardening([[7,8],[7,8],[2,3],[6,10]]),"\n",
    gardening([2,3],[5,6],[3,4],[3,4]),"\n",
    gardening([1,3],[3,5],[4,6],[5,6],[2,4],[7,10]),"\n",
    )

def test_merge():

    print(merge_segments([7,8],[6,10]))
    print(merge_segments([7,8],[7,8]))
    print(merge_segments([7,8],[2,3]))
    print(merge_segments([2,3],[6,10]))
    print(merge_segments([5,6],[6,10]))
    print(merge_segments([6,10],[5,8]))
    print(merge_segments([2,3],[3,4]))
    print(merge_segments([2,5],[3,6]))
    
test_merge()



