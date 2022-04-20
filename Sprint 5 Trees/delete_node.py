# Comment it before submitting
from unittest.mock import NonCallableMagicMock


class Node:  
    def __init__(self, left=None, right=None, value=0):  
        self.right = right
        self.left = left
        self.value = value
    
    def insert(self, value):
        assert type(value) is int

        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value = value)
        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value = value)

    def print_tree(self, space = "->"):
        if self.right:
            self.right.print_tree(space * 2)
        print(space + str(self.value))
        if self.left:
            self.left.print_tree(space * 2)

def get_min(rightsubtree):
    if rightsubtree.left:
        return get_min(rightsubtree.left)
    else:
        return rightsubtree

def traversal_min(root):
    """
    returns left leaf
    """
    while root.left != None:
        root = root.left
    return root

def traversal_max(root):
    """
    returns left leaf
    """
    while root.right != None:
        root = root.right
    return root

def remove(root, key):
    if root == None:
        return root
    
    if root.value > key:
        root.left = remove(root.left, key)
        
    elif root.value < key:
        root.right = remove(root.right, key)
    
    else: #(root.value == key)
        if root.right == None:
            temp = root.left
            root = None
            return temp
        elif root.left == None:
            temp = root.right
            root = None
            return temp
        else:
            min_node = traversal_min(root.right)

            root.value = min_node.value

            root.right = remove(root.right, min_node.value)

    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)

    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


def create_tree(arr):
    root = Node(value=arr[0])
    for i in range(1,len(arr)):
        root.insert(arr[i])
    
    print("-------")
    return root

def test_2():
    print("\nNew tree")
    tree = create_tree([5,3,7,2,4,6,8,0,9])
    tree.print_tree()
    for i in range(2,9):
        print("Trying to remove " ,i)
        new_tree = remove(root=tree,key=i)
        tree.print_tree()
        print("\n-----------------------\n")
        tree = create_tree([5,3,7,2,4,6,8,0,9])

test()
test_2()

