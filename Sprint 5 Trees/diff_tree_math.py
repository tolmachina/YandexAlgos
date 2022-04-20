"""
Total number of possible Binary Search Trees and Binary Trees with n keys
"""
from math import factorial

def tree_count(n: int):
    if n <= 1:
        return 1
    else:
        sumsum: int = 0
        left: int = 0
        right: int = 0
        for i in range(1, n+1):
            left: int = tree_count(i - 1)
            right: int = tree_count(n - i)
            sumsum += left * right
    return sumsum
    
def tree_count_fact(n):
    fact_n = factorial(n)
    top = factorial(2*n)
    bottom = fact_n * fact_n * (n+1)
    return int(top / bottom)

def main():
    stdinin = int(input())
    print(tree_count_fact(stdinin))

if __name__ =='__main__':
    main()
