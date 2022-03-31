"""
Input:
Number of numbers
Numbers to sort

Output:
printing each iteration of sort algo
"""

def bubble_sort(n):
    swap_count = 0
    while True:
        was_swapped = False
        for i in range(len(n) - 1):
            if n[i] > n[i+1]:
                n[i], n[i+1] = n[i+1], n[i]
                was_swapped = True
                swap_count += 1
        if was_swapped == False:
            if swap_count == 0: print(*n)
            break
        print(*n)
    return n

num_lines = int(input())
line = list(map(int, input().split()))

bubble_sort(line)

