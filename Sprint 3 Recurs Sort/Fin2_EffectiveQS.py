"""
id 64725746. Inspired by wikipedias https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme

Time complexity: On average recursion will be as deep as O(log n)(even if array is already sorted because we choose the middle pivot, array will always be split in halves) and on each level of recursion we go thru elements in O(n) time, so it's O(n log n).

Memory complexity: constant O(1), we sort elements in place.
"""


def compare(guy,pivot):
    """
    returns 1 if guy has bigger score or same score and less penalty
    or same score, same penalty but name comes before lexigraphically
    
    returns -1 if guy has less score or same score and more penalty
    or same score, same penalty but name comes after lexigraphically
    
    returns 0 if they are same
    """
    if guy[1] < pivot[1]:
        return 1
    elif guy[1] == pivot[1]:
        if guy[2] > pivot[2]:
            return 1
        elif guy[2] == pivot[2]:
            if guy[0] > pivot[0]:
                return 1
            elif guy[0] == pivot[0]:
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1

def partition_p(arr,left,right):
    pivot_index = (left+right) // 2
    pivot = arr[pivot_index]
    while True:
        while compare(arr[left],pivot) == -1:
            left += 1

        while compare(arr[right],pivot) == 1:
            right -= 1
        
        if left >= right:
            return left
        
        arr[left],arr[right] = arr[right], arr[left]

def quicksort(arr,left,right):
    if left >= right:
        return
    else:
        new_pivot_index = partition_p(arr,left,right)
        quicksort(arr,left,new_pivot_index-1) 
        quicksort(arr,new_pivot_index+1,right)


def main():
    number_of_guys = int(input())
    team = []
    for _ in range(number_of_guys):
        guy = input().split()
        guy[1] = int(guy[1])
        guy[2] = int(guy[2])
        team.append(guy)
    

    quicksort(team,0, len(team) - 1)

    for guy in team:
        print(guy[0])

if __name__ == "__main__":
    main()