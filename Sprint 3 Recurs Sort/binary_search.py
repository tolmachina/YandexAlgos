
def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i
    return -1

def binary_search(keys, query):
    min_ind = 0
    max_ind = len(keys) - 1
    while min_ind <= max_ind:
        mid_ind = int((min_ind + max_ind)/2)
        if query == keys[mid_ind]:
            return mid_ind
        elif query > keys[mid_ind]:
            min_ind = mid_ind + 1
        else:
            max_ind = mid_ind - 1
    return -1

if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

    # queries = [22, 3, 44, 7]
    # [1, 5, 8, 12, 13]
    # [8, 1, 21, 1, 11]
    # for q in queries:
    #     print(binary_search([1,3,7,8,9,12,15],q), end = " ")
