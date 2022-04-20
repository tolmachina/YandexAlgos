from itertools import permutations
from typing import List


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


def collect_trees(all_data: List[List[int]]):
    all_trees = []
    for data in all_data:  # something wrong
        root = Node(data[0])
        for i in range(1,len(data)):
            root.insert(data[i])
        all_trees.append(root)
    return all_trees


def print_trees(all_trees: List[Node], all_data: List[List[int]]):
    for tree, data in zip(all_trees, all_data):
        if data == (2,4,1,3):
            print('Alert')
        print(data)
        tree.print_tree()
        print("-------------------------")


def compare(a: Node, b: Node, swithc_l = True, swithc_r = True):
    if a.value == b.value:
        if a.left and b.left:
            swithc_l = compare(a.left, b.left)
        if a.right and b.right:
            swithc_r = compare(a.right, b.right)
        return swithc_r and swithc_l
    else:
        return False


def tree_count(number):
    all_data = list(permutations(range(1,number+1)))
    all_trees = collect_trees(all_data)
    # print_trees(all_trees=all_trees, all_data = all_data)
    non_uniques_trees = set()
    non_uniques_data = set()
    for i in range(len(all_trees)):
        for j in range(i+1, len(all_trees)):
            if compare(all_trees[i], all_trees[j]):
                non_uniques_trees.add(all_trees[i])
                non_uniques_data.add(all_data[i])
                break
    count = len(all_trees) - len(non_uniques_trees)
    # print("not unique")
    # print_trees(all_trees=non_uniques_trees, all_data=non_uniques_data)
    return count

def main():
    stdinin = int(input())
    print(tree_count(stdinin))

if __name__ =='__main__':
    main()



# def test_compare():
#     tree123 = Node(1)
#     tree123.insert(2)

#     tree123.insert(3)

#     tree213 = Node(2)
#     tree213.insert(1)
#     tree213.insert(3)

#     tree231 = Node(2)
#     tree231.insert(3)
#     tree231.insert(1)

#     print_trees([tree123,tree213,tree231], [[1,2,3],[2,1,3],[2,3,1]])
#     assert(compare(tree123, tree213) == False)
#     assert(compare(tree213, tree231) == True)
# def test_a():
#     all_data = tree_count(3)
#     print_trees(all_data)

# def test_b():
#     all_trees = collect_trees(tree_count(3))

#     a = all_trees[2]
#     b = all_trees[3]
#     c = Node(5)
#     c.insert(4)
#     c.insert(6)
#     print(a)
#     print(b)
#     print(c)
#     print("Are equal?", compare(a,b))
#     print("Are equal?", compare(a,c))
    
    

# # test_b() 

# def test():
#     # assert(tree_count(2)) == 2
#     assert(tree_count(3)) == 5
#     assert(tree_count(4)) == 14

# test()
