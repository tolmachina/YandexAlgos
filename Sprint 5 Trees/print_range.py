# do not declare Node in your submit-file 

class Node: 
    def __init__(self, left=None, right=None, value=0): 
        self.value = value 
        self.right = right 
        self.left = left 
################# 
def print_range(node, l, r):
    """
    node is a root
    """

    # if node.value < l:
    #     if node.right:
    #         print_range(node.right, l, r)
    #     else:
    #         lowest_value = node.value
    # else:
    #     if node.left:
    #         print_range(node.left, l, r)
    #     else:
    #         lowest_value = node.value

    # print(lowest_value)

    def printLMR(node,l,r):
        if node.value >= l:
            if node.left:
                printLMR(node.left, l, r)
        
        if l <= node.value <= r:
            print(node.value)
        
        if node.value <= r:
            if node.right:
                printLMR(node.right,l , r)
    
    printLMR(node, l, r)




def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8

test()
