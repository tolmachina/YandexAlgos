from typing import List

def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes

def factorize(number: int) -> List[int]:
    primes = get_least_primes_linear(number)
    res = []
    while number > 1.0:
        i = 0
        j = 0
        while i < len(primes) - 1:
            if number % primes[i] == 0:
                number /= primes[i]
                res.append(primes[i])
                break
            i += 1
    return res
        

result = factorize(int(input()))
print(" ".join(map(str, result)))
