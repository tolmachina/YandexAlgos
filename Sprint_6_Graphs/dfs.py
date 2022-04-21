""" 
Задан неориентированный граф. Обойдите с помощью DFS все вершины, достижимые из заданной вершины s, и выведите их в порядке обхода, если начинать обход из s.
Формат ввода

В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа. Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n). В последней строке дан номер стартовой вершины s (1 ≤ s ≤ n). В графе нет петель и кратных рёбер.
Формат вывода

Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной вершины её соседи будут рассматриваться в порядке возрастания (то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).
"""
def dfs(v: int) -> None:
    """dfs prints nodes

    Args:
        v (int): _description_
    """
    print(v, end =' ')
    colors[v] = 'gray'
    for w in graph[v]:
        if colors[w] == 'white':
            dfs(w)
    colors[v] = 'black'
    
def dfs_iter(start_vertex: int) -> None:
    """Depth-first Search

    Args:
        start_vertex (int): index of node in graph array
    """
    stack = []
    stack.append(start_vertex)
    while stack:
        v = stack.pop()
        if colors[v] == 'white':
            colors[v] = 'gray'
            stack.append(v)
            for w in graph(v):
                if colors[w] =='white':
                    stack.append(w)
        elif colors[v] == 'gray':
            colors[v] = 'black'

def MainDFS():
    for i in range(n):
        if colors[i] == 'white':
            dfs(i)


line_one = input().split()
n = int(line_one[0])
m = int(line_one[1])
edges = []
for i in range(m):
    edge = list(map(int, input().split()))
    edges.append(edge)
s = int(input())

colors = []
for i in range(n+1):
    colors.append('white')

graph = [[] for x in range(n+1)]

for edge in edges:
    v_a = edge[0]
    v_b = edge[1]
    graph[v_a].append(v_b)
    graph[v_b].append(v_a)

for v in graph:
    v.sort()

dfs(s)

print()
