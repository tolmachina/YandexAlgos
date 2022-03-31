from common_subarray import common_subarray

def A():
    vector_a = [1, 2, 3, 2, 1]
    vector_b = [3, 2, 1, 5, 6]
    assert common_subarray(vector_a, vector_b) == 3


def B():  
    vector_a = [1, 2, 3, 4, 5]
    vector_b = [4, 5, 9]
    assert common_subarray(vector_a, vector_b) == 2


"""
1
1
1
1




"""