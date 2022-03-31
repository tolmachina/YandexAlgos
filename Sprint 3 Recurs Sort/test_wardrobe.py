from wardrobe import count_sort

def test():
    assert(count_sort([2,1,1,2,0,2]) == [0,1,1,2,2,2] )
    assert(count_sort([2,1,2,0,1]) == [0,1,1,2,2] )
    assert(count_sort([0,2,1,2,0,0,1]) == [0,0,0,1,1,2,2] )

test()