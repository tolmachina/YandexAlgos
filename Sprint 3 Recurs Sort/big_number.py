"""
Get the biggest number from list 2, 11.
211 > 112.

iterate over list from index 1.
pick the number and compare with previous one.
"""

from typing import List


def compare(a, b) -> bool:
    """
    stringify two integers and glue them together
    list 2, 11.
    211 > 112.
    """
    a, b = str(a), str(b)
    return int(a + b) > int(b + a)
    

def test_compare():
    test_a = [1,783,2]
    test_b = [1,783,2]

    for a in test_a:
        for b in test_b:
            print(f"{a} is bigger then {b}, {compare(a,b)}")

def insertion_sort(array: List) -> None:
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and compare(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    print( "".join(list(map(str, array )) ))

def test():
    insertion_sort([15,56,2])
    insertion_sort([1,783,2])
    insertion_sort([2,4,5,2,10])
    insertion_sort([9,10,1,1,1,6])

# test_compare()
# test()
num_lines = int(input())
line = list(map(int, input().split()))

insertion_sort(line)
