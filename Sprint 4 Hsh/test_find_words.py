import sys
from find_words import *

def max_routine(number, array: List[int] = []):
    if len(array) == 0:
        array.append(number)
    else:
        if len(array) > 5:
            array.pop()
        for i in range(len(array)):
            if array[i] < number:
                array.insert(i, number)
            elif array[i] == number:
                array.insert(i+1, number)
    return array


def search(docs: List[dict], requests: List[int]):
    for query in requests:
        relevancy = 0
        doc_num = 1 
        table = {}
        for doc in docs:
            relevancy = get_relevancy(doc, query)
            if relevancy != 0:
                table[doc_num] = relevancy
            doc_num += 1
        print(*sorted(table, key=table.get, reverse=True)[:5])

def process_doc(doc):
    memo = {}
    for word in doc:
        if word not in memo:
            memo[word] = 1
        else:
            memo[word] += 1
    return memo


def search2(docs: List[dict], request: set):
    relevancy = 0
    doc_num = 1 
    table = {}
    for doc in docs: #O(N) looks at a line
        relevancy = get_relevancy(doc, request)
        if relevancy != 0:
            table[doc_num] = relevancy
        doc_num += 1
    return table

def get_relevancy(doc: dict, request: str):
    relevancy = 0
    memo = {}
    for word in request: #O(N)
        if word not in memo:
            if word in doc:
                memo[word] = doc[word]
    relevancy = sum(memo.values()) #O(N)
    return relevancy

    

def test():
    my_line = "i love coffe with milk and sugar"
    my_request = "mary likes black coffe without milk"
    relevancy = get_relevancy(my_line, my_request)
    print(relevancy)


# top_five = sorted(table, key=table.get, reverse=True)[:5]
# top_five_heap = heapq.nlargest(5, table,key=table.get)
