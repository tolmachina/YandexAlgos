import sys

class LinkedList:
    def __init__(self):
        self.head = None

class OtherNode:
    def __init__(self, value=None, link=None):
        self.value = value
        self.next = link

    def __repr__(self):
        return self.value

class Node:
    def __init__(self, value=None, link=None):
        self.value = value
        self.next = link

    def __repr__(self):
        return self.value


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")

def get_node_by_index(node, index):
        while index:
                node = node.next
                index -= 1
        return node

def insert_node(head, index, value):
        new_node = Node(value)
        if index == 0:
                new_node.next = head
                return new_node
        previous_node = get_node_by_index(head, index-1)
        new_node.next = previous_node.next
        previous_node.next = new_node
        return head


dark_matter = "VeryDark"
yellow = OtherNode(value="yellow", link=OtherNode())
green = Node(value="green", link=yellow)
blue = Node(value="blue", link=green)

print("size blue: ", sys.getsizeof(blue), "Bytes")
print("size green: ", sys.getsizeof(green), "Bytes")

print_linked_list(blue)
print_linked_list(green)
