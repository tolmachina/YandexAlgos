rosseta = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

def how_many_left(n, i):
    return len(n) - i

def gen_letters(n, numbers, letters, i, j):
    if n == 0:
        print(letters)
    else:
        if (j+1) == len(rosseta[numbers[i]]):
            i = 0
            j = 0
        if i < len(numbers):
            gen_letters(n - 1, numbers, letters + rosseta[numbers[i]][j], i+1, j)
        if j < len(rosseta[numbers[i]]):
            gen_letters(n - 1, numbers, letters + rosseta[numbers[i]][j], i, j+1)

def gen_letters_iter(result, n, numbers, i, j, digit):
    rosseta = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if n == 0:
        print(result)
        i = 0
        j = 0
        n = 3
        result = ""

    else:
        result += rosseta[digit][j]
        i += 1
        n -= 1
        if i < len(numbers):
            next_digit = numbers[i]
        else:
            next_digit = numbers[0]
        gen_letters_iter(result, n, numbers, i, j,  next_digit)
        
        j += 1

    return result



def gen_new(numbers):
    rosseta = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    
    def rec_gen (n, results):
        if n == 0:
            print(results)
        tmp_A = results
        tmp_b = rosseta['next_digit']
        rec_gen()

    tmp_A = rosseta[numbers[0]]
    tmp_B = rosseta[numbers[1]]
    results = []
    for x in tmp_A:
        for y in tmp_B:
            res = x + y
            results.append(results)
    
    rec_gen(len(numbers), results)

