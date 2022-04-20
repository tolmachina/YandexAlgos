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


    def print_tree(self, space = "->"):
        if self.right:
            self.right.print_tree(space * 2)
        print(space + str(self.value))
        if self.left:
            self.left.print_tree(space * 2)

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

def insert(root, key):
    if key >= root.value:
        if root.right:
            insert(root.right, key)
        else:
            new_node = Node(value=key)
            root.right = new_node
            
    if key < root.value:
        if root.left:
            insert(root.left, key)
        else:
            new_node = Node(value=key)
            root.left = new_node
    return root        

    
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
