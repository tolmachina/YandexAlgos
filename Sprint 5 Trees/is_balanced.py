# Comment it before submitting
class Node:  
    def __init__(self, value, left=None, right=None):  
        self.value = value  
        self.right = right  
        self.left = left
    
    def __str__(self):
        if self != None:
            return "Value:" + str(self.value) + "\nLeft Child:" + str(self.left.value) + "\nRight Child:" + str(self.right.value)    
        else:
            return str(None)
    
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)

    def print_tree(self, space = "->"):
        if self.right:
            self.right.print_tree(space * 2)
        print(space + str(self.value))
        if self.left:
            self.left.print_tree(space * 2)


def solution(root):
    count_left = 0
    count_right = 0
    val = root.value
    total_left = 0

    def heigh(root, h=0):
        if root == None:
            return 0
        else:
            return max(heigh(root.left, h), heigh(root.right, h)) + 1

    def count_nodes(root):
        height_left = heigh(root.left)
        height_right = heigh(root.right)
        result = abs(height_right - height_left) < 2
        if result == False:
                return False
        if root.left:
            result = count_nodes(root.left)
            if result == False:
                return False
        if root.right:
            result = count_nodes(root.right)
            if result == False:
                return False

        return result
    
    l = count_nodes(root)
    return l


def heigh(root, h=0):
    if root == None:
        return 0
    else:
        h_l = heigh(root.left, h + 1)
        h_r = heigh(root.righ, h + 1)
        return max(h_l, h_r)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)

def test3():
    n12 = Node(12, None, None)
    n4 = Node(4, n12, None)
    n8 = Node(8, None, None)
    n7 = Node(7, n4,n8)
    n2 = Node(2, None, None)
    n0 = Node(0, n2, n7)
    # n0.print_tree()
    assert (solution(n0) == False)

def test2():
    node6 = Node(6, None, None)
    node7 = Node(7, None, None)
    node8 = Node(8, None, None)
    node5 = Node(5, None, None)
    node4 = Node(4, node7, node8)
    node3 = Node(3, node5, node6)
    node2 = Node(2, None, node4)
    node1 = Node(1, node3, None)    
    node0 = Node(0, node1, node2)

    # node0.print_tree()
    assert (solution(node0) == False)

test()
test3()
test2()