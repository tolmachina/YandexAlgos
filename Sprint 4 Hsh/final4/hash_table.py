
class myhashtable():

    """
    Hash table based on python list.
    Collisions are resolved with linked list.
    Hash function is basic.

    """
    def __init__(self, N = 100000):
        self.N = N
        self.buckets = [None] * N

    def put(self, key, value):
        i = self.hash(key)
        if self.buckets[i] is None:
            self.buckets[i] = [(key, value)]
        else:
            self.linkedlist = self.buckets[i]
            for i in range(len(self.linkedlist)):
                if self.linkedlist[i][0] == key:
                    self.linkedlist[i] = (key, value)
                    return
            self.linkedlist.append((key, value))

    def get(self, key):
        i = self.hash(key)

        if self.buckets[i] == None:
            return None

        if len(self.buckets[i]) == 1:
            self.bucket = self.buckets[i] 
            if self.bucket[0][0] == key:
                return self.bucket[0][1]
            else: return None
        
        else:
            self.linked_list = self.buckets[i] 
            for i in range(len(self.linked_list)):
                if self.linked_list[i][0] == key:
                    return self.linked_list[i][1]
            return None

    def delete(self, key):
        i = self.hash(key)
        if self.buckets[i] == None:
            return None
        if len(self.buckets[i]) == 1:
            if self.buckets[i][0][0] == key:
                value = self.buckets[i][0][1] 
                self.buckets[i] = None
                return value
            else:
                return None
        else:
            self.linked_list = self.buckets[i] 
            for i in range(len(self.linked_list)):
                if self.linked_list[i][0] == key:
                    value = self.linked_list[i][1]
                    del self.linked_list[i]
                    return value
            return None

    def hash(self, key):
        hash_num = key % self.N
        return hash_num
    

        


def main():
    my_d = myhashtable()
    n = int(input())
    for _ in range(n):
        command = input().split()
        if command[0] == 'get':
            print(my_d.get(int(command[1])))
        elif command[0] == 'put':
            my_d.put(key = int(command[1]), value = int(command[2]))
        elif command[0] == 'delete':
            print(my_d.delete(key = int(command[1])))

if __name__ == '__main__':
    main()
