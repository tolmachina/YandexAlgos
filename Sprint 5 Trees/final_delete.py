"""
id 67358489

Delete a node in a binary tree.

Time Complexity - O(h) h is height of a tree.

"""

def traversal_min(root):
    """
    returns last left leaf
    """
    while root.left != None:
        root = root.left
    return root

def remove(root, key):
    #base case
    if root == None:
        return root
    
    # choosing which subtree to look into
    if root.value > key:
        root.left = remove(root.left, key)
        
    elif root.value < key:
        root.right = remove(root.right, key)
    
    # if key is found
    else: #(root.value == key)
        
        #if no children or no children on one side
        if root.right == None:
            temp = root.left
            root = None
            return temp
        
        elif root.left == None:
            temp = root.right
            root = None
            return temp
        
        #if both children
        else:
            min_node = traversal_min(root.right)
            root.value = min_node.value
            root.right = remove(root.right, min_node.value)

    return root