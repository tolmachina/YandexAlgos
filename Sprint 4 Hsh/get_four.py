"""
У Гоши есть любимое число S. Помогите ему найти все уникальные четвёрки чисел в массиве, которые в сумме дают заданное число S.

Формат ввода:

В первой строке дано общее количество элементов массива n (0 ≤ n ≤ 1000).
Во второй строке дано целое число S  .
В третьей строке задан сам массив. Каждое число является целым и не превосходит по модулю 10**9.

Формат вывода:

В первой строке выведите количество найденных четвёрок чисел.
В последующих строках выведите найденные четвёрки. Числа внутри одной четверки должны быть упорядочены по возрастанию. Между собой четвёрки упорядочены лексикографически.

"""


import numbers
from typing import List

def f_sum(s, vector: List):
    vector.sort()
    return ksum(s, vector, 4)

def ksum(k: int, target: int, vector: List):
    if k == 2:
        return two_sum(target, vector)


def two_sum(target: int, vector: List[int]):
    # vector.sort()
    # print('sorted vec', vector)
    memo = set()
    result = []
    for num in vector:
        if (target - num) in memo:
            result.append((target - num, num))
        else:
            memo.add(num)
            # print('memo: ', memo)
    return result

def tri_sum(target: int, vector: List[int]):
    vector.sort()
    # print('sorted_vector', vector)
    memo = set()
    result = set()
    for i in range(len(vector)):
        for j in range(i+1, len(vector)):
            if (target - vector[i] - vector[j]) in memo:
                result.add((target-vector[i]-vector[j],vector[i],vector[j]))
       
        memo.add(vector[i])
                # print('memo', memo)
    return result

def four_sum(target: int, vector: List[int]):
    # vector.sort()
    # print('sorted_vector', vector) 
    memo = set()
    result = set()
    for i in range(len(vector)):
        for j in range(i+1, len(vector)):
            for q in range(j+1, len(vector)):
                y = (target - vector[i] - vector[j] - vector[q])
                if y in memo:
                    result.add(tuple(sorted((y ,vector[i], vector[j], vector[q]))))
        memo.add(vector[i])
    return result

def four_sum_table(target: int, vector: List[int]):
    if len(vector) < 4:
        return 0
    vector.sort()
    # print('sorted_vector', vector) 
    memo = {sum(vector[0:2]): (vector[0],vector[1])}
    result = set()
    for i in range(2, len(vector)):
        for j in range(i + 1, len(vector)):
            y = target - vector[i] - vector[j]
            if y in memo:
                z, x = memo[y]
                result.add(tuple (sorted ((vector[i], vector[j], z, x)) ))
        for w in range(i-1, -1, -1):
            key = sum((vector[w], vector[i]))
            memo[key]  = (vector[w], vector[i])
            # print('memo', memo)
    return result  
    

def two_sum_points(target: int, massive: List[int]):
    result =[]
    lo, hi = 0, len(massive) - 1

    while lo < hi:
        curr_sum = massive[lo] + massive[hi]
        if curr_sum == target:
            result.append((massive[lo], massive[hi]))
        elif curr_sum < target:
            hi += 1
        else:
            lo += 1
    
    return result

    
# vector = [5,2,8,1,1,3,4,4]
# target = 10
# k = 2
# print(four_sum(target, vector))

n = int(input()) #quantity of elements
s = int(input()) #target number
vector = input().split()

if n<4:
    print(0)
else: 
    vector = list(map(int ,vector))
    set_of_sums = list(four_sum_table(s, vector))
    set_of_sums.sort()
    print(len(set_of_sums))
    for set in set_of_sums:
        print(*set)
