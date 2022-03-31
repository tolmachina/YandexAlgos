from py import test


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

    def print_tree(self, space = "  "):
        if self.right:
            self.right.print_tree(space * 2)
        # print()
        print(space + str(self.value))
        if self.left:
            self.left.print_tree(space * 2)
        
    
def find_value(node, max_val):
        if node.value > max_val:
            max_val = node.value
        if node.left:
            left_val = find_value(node.left, max_val)
            if left_val > max_val:
                max_val = left_val
        
        if node.right:
            right_val = find_value(node.right, max_val)
            if right_val > max_val:
                max_val = right_val
    
        return max_val
def test_print_tree():
    one = Node(5)

    one.insert(1)
    one.insert(9)

    one.insert(0)
    one.insert(2)

    one.insert(7)
    one.insert(10)

    print(one)
    one.print_tree()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    # print(root)

# test_print_tree()
