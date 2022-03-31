def insertion_sort(array):
    for i in range(1, len(array) - 1):
        item_to_insert = array[i] #extrac item from array
        j = i
        while j > 0 and item_to_insert < array[j - 1]: #compare that item with previous one
            array[j] = array[j-1] # overwrite previous with current
            j -= 1 #iterate down
        array[j] = item_to_insert #return item on place of current
        print('step {i},sorted {i+1} elements: {array}')

