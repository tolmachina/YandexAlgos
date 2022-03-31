import sys
from typing import List

def weather_chaos(n, days):
    if n == 1:
        return 1
    temp = 0
    if days[0] > days[1]:
        temp += 1
    if days[-1] > days[-2]:
        temp += 1
    for i in range(1, n - 1):
        if days[i - 1] < days[i] > days[i + 1]:
            temp += 1
    return temp

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return n, temperatures

def main():
    n, temperatures = read_input()

    print(weather_chaos(n, temperatures))

if __name__ == '__main__':
    main()


