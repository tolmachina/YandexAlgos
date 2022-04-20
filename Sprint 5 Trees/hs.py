# sort by prob, fine, name

"""
id 67590262

Sort list of persons with heapsort.

I have created class person and overloaded "<" operator to compare persons by 
number of solved problems and if they equal, by number of a fine and if equal, by name. Highest score has a person with most problems solved, least number of a fine and his name comes earlier in alphabetical order.

Sorting is done with heapsort.
Link https://practicum.yandex.ru/learn/algorithms/courses/7f101a83-9539-4599-b6e8-8645c3f31fad/sprints/24944/topics/e7dbf42a-fd5a-434b-990d-9cfe0e3a10c8/lessons/116802f2-0842-4195-9d12-13e7bf0efad1/

Input array of persons is transformed into Priority Queue using Binary Heap. Then top elements of priority queue are taken off and added to initially empty sorted array. Priority queue is restructed and we repeat the loop until queue is empty.

Time Complexity is O(nlogn) in worst case as insertion and deletion from binary heap takes O(nlogn) time.
Space Complexity is O(n) as we need space for an array of n elements.
"""
class person():
    def __init__(self, name: str, prob: int, fine: int):
        self.name = name
        self.prob = prob
        self.fine = fine

    def __str__(self):
        return f"{self.name} {str(self.prob)} {str(self.fine)}\n"
    
    def __lt__(self, other):
        if self.prob < other.prob:
            return True
        elif self.prob > other.prob:
            return False
        else:
            if self.fine < other.fine:
                return False
            elif self.fine > other.fine:
                return True
            else:
                if self.name < other.name:
                    return False
                elif self.name > other.name:
                    return True
                else:
                    assert self.name != other.name, "Person's names not Unique"


def heap_add(heap, key):
    index = len(heap)
    heap.append(key)
    sift_up(heap, index)


def sift_up(heap, idx):
    if idx == 1:
        return idx
    parent_index = idx // 2
    if heap[parent_index]  < heap[idx]:
        heap[parent_index], heap[idx] = heap[idx], heap[parent_index]
        return sift_up(heap, parent_index)
    else:
        return idx
    

def pop_max(heap):
    if len(heap) > 2:
        result = heap[1]
        heap[1] = heap.pop()
        sift_down(heap, 1)
        return result
    else:
        return heap.pop()


def sift_down(heap: list, index: int):
    # indexes of potential lef and right children
    left = 2 * index
    right = 2 * index + 1
    # check if children at all possible
    if (len(heap)-1) < left:
        return index
    # check if right child is there and use it if it bigger
    if (right < len(heap)) and (heap[left] < heap[right]):
        index_largest = right
    else:
        index_largest = left
    # do swapperu and move to next sift
    if heap[index ]< heap[index_largest]:
        heap[index], heap[index_largest] = heap[index_largest], heap[index]
        return sift_down(heap, index_largest)
    # if we swapped enough
    else:
        return index


def heap_get_max_priority(heap):
    """
    input: heap
    return: heap minus lowest element at heap[1], that lowest element
    """
    lowest_elem = pop_max(heap)
    return heap, lowest_elem.name


def heapsort(all_persons):
    heap = [None]

    for p in all_persons:
        heap_add(heap, p)
    sorted_array = []

    while len(heap) > 1:
        heap, top = heap_get_max_priority(heap)
        sorted_array.append(top)
    return sorted_array


def main():
    n = int(input())

    all_persons = []

    for i in range(n):
        line = input().split()
        name = line[0]
        prob = int(line[1])
        fine = int(line[2])
        newperson = person(name, prob, fine)
        all_persons.append(newperson)

    sorted_array = heapsort(all_persons)

    for name in sorted_array:
        print(name)


if __name__ == "__main__":
    main()






