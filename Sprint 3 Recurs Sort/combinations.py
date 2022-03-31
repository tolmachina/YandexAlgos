"""
input: numbers 2..9 string less then 10 symbols.
output: all possible encoded combinations separated by space
"""

def cartesian_product(vector_A, vector_B):
    products =[]
    for x in vector_A:
        for y in vector_B:
            result = x + y
            products.append(result)
    return products

def wrapy_snappy(number):
    rosseta = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    database =[]
    for dig in number:
        database.append(rosseta[dig])
    
    return database

def multi_product(database):
    result = database[0]
    for i in range(1, len(database)):
        result = cartesian_product(result, database[i])
    print(*result)

numbers = input()
combination = ""

multi_product(wrapy_snappy(numbers))
