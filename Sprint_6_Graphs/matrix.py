"""
Алла успешно справилась с предыдущим заданием, и теперь ей дали новое. На этот раз список рёбер ориентированного графа надо переводить в матрицу смежности. Конечно же, Алла попросила вас помочь написать программу для этого.
Формат ввода

В первой строке дано число вершин n (1 ≤ n ≤ 100) и число рёбер m (1 ≤ m ≤ n(n-1)). В следующих m строках заданы ребра в виде пар вершин (u,v), если ребро ведет от u к v.
Формат вывода

Выведите матрицу смежности n на n. На пересечении i-й строки и j-го столбца стоит единица, если есть ребро, ведущее из i в j.
"""


line_one = input().split()
n = int(line_one[0])
m = int(line_one[1])
edges = []
for i in range(m):
    edge = list(map(int, input().split()))
    edges.append(edge)


graph = [[0 for y in range(n)] for x in range(n)]

for edge in edges:
    v_a = edge[0]
    v_b = edge[1]
    graph[v_a - 1][v_b - 1] = 1

for i in range(len(graph)):
    for j in range(len(graph[0])):
        print(graph[i][j], end=' ')
    print()

# 1: 2,3; 2: 4,5; 3: None