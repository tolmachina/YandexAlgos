from Fin1_BrokenArray import broken_search

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 21) == 1
    arr = [5,1]
    assert broken_search(arr, 1) == 1
    arr = [1,2,3,5,6,7,9,0]
    assert broken_search(arr, 1) == 0

test()
