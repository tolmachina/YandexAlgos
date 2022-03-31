"""
66178998

Input:
n - number of docks in a database(1<= n<= 10**4)
Next n lines are docs. Each doc is <= 1000 symbols.
Never empty

m - number of search requests.
Next m lines are searches. Each search no longer then 100 symbols.


Output:
On each search request show relevant doc numbers. Max five per request.
Doc numbers start with 1.

"i love coffe with milk and sugar"

example:

3
i like dfs and bfs
i like dfs dfs
i like bfs with bfs and bfs
1
dfs dfs dfs dfs bfs

out:
3 1 2

Solution:

Process all documents in dict structure:
{'word': {doc_num1: freq1, docnum2:freq2}}
From that structure calculate table:
'{doc_num1: relevancy}', sort that dict and get top 5. 

Time Complexity: - O(n), n - number of words
Memory Comlexity: - O(n), n - number of words

"""
import heapq
from typing import List

def get_data_and_search(): 
    """
    Main function that parses input data and calls search
    """
    n = int(input()) 
    docs = []
    big_memo = {} # structure for big_memo {'coffe': {doc_num1: freq1, docnum2:freq2}}
    doc_count = 1
    for _ in range(n):
        big_memo = proceess_all_docs(input().split(), big_memo, doc_count) # O(n)
        doc_count += 1
    m = int(input())
    for _ in range(m):
        req = set(input().split()) #O(n) + O(n)
        table = search_big_memo(big_memo, req)
        print_table(table)
    

def proceess_all_docs(doc, big_memo, doc_count):
    for word in doc: #O(N)
        if word not in big_memo:
            big_memo[word] = {doc_count: 1}
        else:
            big_memo[word][doc_count] = big_memo[word].get(doc_count, 0) + 1
    return big_memo



def search_big_memo(big_memo:dict, request: set):
    # structure for big_memo {'coffe': {doc_num1: freq1, docnum2:freq2}}
    table = {}
    for word in request:
        if word in big_memo:
            little_memo = big_memo[word]
            for k,v in little_memo.items():
                if k not in table:
                    table[k] = v
                else: table[k] += v
    return table

def print_table(table: dict):
    try:
        """
        I need to sort table before printing five top results
        """
        table = dict(sorted(table.items())) #O(nlogn) thats a bottleneck
        
        for _ in range(5): # get five max value
            best = max(table,key=table.get)
            print(best, end = ' ')
            del table[best]

    except ValueError:
        pass
    finally:
        print()

if __name__ == '__main__':
    get_data_and_search()