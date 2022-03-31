# # Comment it before submitting
# class Node:  
#     def __init__(self, value, left=None, right=None):  
#         self.value = value  
#         self.right = right  
#         self.left = left


def solution(root):
    memo = set()
    switch = True
    def is_ok(root, memo, switch):
        if root.value not in memo:
            memo.add(root.value)
        else:
            switch = False
            return memo, switch
        if root.left:
            if root.left.value < root.value:
                memo, switch = is_ok(root.left, memo, switch)
            else:
                switch = False
                return memo, switch
        if root.right:
            if root.right.value > root.value:
                memo, switch = is_ok(root.right, memo, switch)
            else:
                switch = False
                return memo, switch
        return memo, switch

    memo, switch = is_ok(root, memo, switch)
    return switch

    




def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

test()