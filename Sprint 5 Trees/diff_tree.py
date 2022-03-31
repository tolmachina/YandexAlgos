from trees import Node
from math import factorial
from itertools import permutations

def tree_count(number):
    data = list(permutations(range(1,number+1)))
    return data

def print_trees(all_data):
    for data in all_data:
        root = Node(data[0])

        for i in range(1,len(data)):
            root.insert(data[i])
        
        root.print_tree()
        print("@@@@")

def collect_trees(all_data):
    all_trees = []
    for data in all_data:
        root = Node(data[0])

        for i in range(1,len(data)):
            root.insert(data[i])
        
        all_trees.append(root)

    return all_trees

def compare(a, b):
    if a.value == b.value:
        if a.left and b.left:
            compare(a.left, b.left)
        if a.right and b.right:
            compare(a.right, b.right)
        return True
    else:
        return False

def test_a():
    all_data = tree_count(3)
    print_trees(all_data)

def test_b():
    all_trees = collect_trees(tree_count(3))

    a = all_trees[2]
    b = all_trees[3]
    c = Node(5)
    c.insert(4)
    c.insert(6)
    print(a)
    print(b)
    print(c)
    print("Are equal?", compare(a,b))
    print("Are equal?", compare(a,c))
    
    

test_b()

def test():
    assert(tree_count(2)) == 2
    assert(tree_count(3)) == 5
    assert(tree_count(4)) == 14
