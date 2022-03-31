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


hasher = Map()

hasher.set(key="vodka", value=3.15)

print(hasher.get(key="vodka"))

