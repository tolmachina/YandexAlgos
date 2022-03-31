from random import randint

def partition_p(arr,left,right):
    pivot_index = (left+right) // 2
    pivot = arr[pivot_index]
    while True:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1
        if left >= right:
            print("left, right", (left,right))
            return left
        arr[left],arr[right] = arr[right], arr[left]
        print("swapped", arr)

def quicksort(arr,left,right):
    if left < right:
        new_pivot_index = partition_p(arr,left,right)
        quicksort(arr,left,new_pivot_index) 
        quicksort(arr,new_pivot_index+1,right)
    return arr

x = quicksort([76,9,55,14,2,4,5],0,6)
print(x)
x = quicksort([1,2,3,4,9,5,6,7],0,7)
print(x)


def test_qs_for_final():
    arr = [['sam', 9,100], ['adamas',4,111],['adam',5,100], ['adsz',3, 100], ['tolya', 6, 100]]
    quicksort(arr, 0, len(arr)-1)
    print("sorted in-place",arr )
    arr = [['sam', 9,99], ['das',9,111],['adam',9,98], ['adsz',9, 112], ['tolya', 9, 115]]
    quicksort(arr, 0, len(arr)-1)
    print("sorted in-place",arr )
    arr = [['alla',0,0],['gena',0,0],['gosha',0,0],['rita',0,0],['timofey',0,0]]
    quicksort(arr,0,len(arr)-1)
    print("sorted in-place",arr )
    arr = [['alla',4,100],['gena',6,1000],['gosha',2,90],['rita',2,90],['timofey',4,80]]
    quicksort(arr,0,len(arr)-1)
    print("sorted in-place",arr )
