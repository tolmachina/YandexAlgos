def heap_add(heap, key):
    index = len(heap)
    heap.append(key)
    sift_up(heap, index)

def sift_up(heap, idx):
    if idx == 1:
        return idx
    parent_index = idx // 2
    if heap[parent_index] < heap[idx]:
        heap[parent_index], heap[idx] = heap[idx], heap[parent_index]
        return sift_up(heap, parent_index)
    else:
        return idx
    
    
def pop_max(heap): # check if works
    result = heap[1]
    heap[1] = heap[len(heap) - 1]

    sift_down(heap, 1)
    return result

def sift_down(heap: list, index: int):
    # indexes of potential lef and right children
    left = 2 * index
    right = 2 * index + 1
    # check if children at all possible
    if (len(heap)-1) < left:
        return index
    # check if right child is there and use it if exists
    if (right < len(heap)) and (heap[left] < heap[right]):
        index_largest = right
    else:
        index_largest = left
    # do swapperu and move to next sift
    if heap[index] < heap[index_largest]:
        heap[index], heap[index_largest] = heap[index_largest], heap[index]
        return sift_down(heap, index_largest)
    # if we swapped enough
    else:
        return index

def heapsort(array):
  # Создадим пустую бинарную кучу.
  heap = []
  
  # Вставим в неё по одному все элементы массива, сохраняя свойства кучи.
  for item in array:
    heap_add(heap, item)   # псевдокод для heap_add можно посмотреть в прошлом уроке
  
  # Будем извлекать из неё наиболее приоритетные элементы, удаляя их из кучи.
  sorted_array = []
  i = 0
  while heap:
    heap, sorted_array[i] = heap_get_max_priority(heap) 
    # псевдокод для heap_get_max_priority можно посмотреть в прошлом уроке
    i += 1 


def test_sift_up():
    sample = [-1, 12, 6, 8, 3, 5, 7, 10]
    assert sift_up(sample, 7) == 3

def test_sift_down():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5

    sample = [-1, 90, 70, 50]
    sample[1] -= 1
    assert sift_down(sample, 1) == 1
    sample[3] -= 1
    assert sift_down(sample, 3) == 3
    sample[2] -= 1
    assert sift_down(sample, 2) == 2
    sample[1] -= 25
    assert sift_down(sample, 1) == 2
    sample[1] -= 40
    assert sift_down(sample, 1) == 2
    sample[1] -= 60
    assert sift_down(sample, 1) == 3
    assert sample == [-1, 49,29,4]

test_sift_down()

