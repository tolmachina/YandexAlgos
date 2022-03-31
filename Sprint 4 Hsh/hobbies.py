class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Map:
    def __init__(self):
        self.pairs = []
    
    def get(self, key):
    
        for pair in self.pairs:
            if pair.key == key:
                return pair.value
        return None
    
    def set(self, key,value):
        for pair in self.pairs:
            if pair.key == key:
                pair.value = value
                return
        
        self.pairs.append(Pair(key=key,value=value))

    def print_keys(self):
        for pair in self.pairs:
            print(pair.key)

def solution_1():
    n = int(input())

    database = Map()

    for i in range(n):
        line = input()
        x = database.get(line)
        if x == None:
            database.set(key=line,value=1)
        else:
            continue
        
    database.print_keys()

def solution_2():
    n = int(input())
    database = {}

    for i in range(n):
        line = input()
        if line in database:
            continue
        else:
            database[line] = 1

    for k in database.keys():
        print(k)

solution_2()