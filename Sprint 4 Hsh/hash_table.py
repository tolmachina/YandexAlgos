
class myhashtable():

    """
    66108912
    Hash table based on python list.
    Collisions are resolved with linked list.
    Hash function is basic.

    Table has a fixed size of N(adjustable by user).
    Internally it creates a number on N buckets, each bucket contains
    tuple (key, value). To put, get or delete value takes from O(1) to O(y).
    O(1) happens if particular bucket is empty.
    O(y) if bucket is taken and y is number of items in that bucket.
    To get an index of bucket key is hashed. Function hash(key) gives an index of
    bucket in range 0, N.

    Hash table will take at O(N + U) memory. N - is size of internal array
    and U is amout of user infromation in it. There is no restrictions on value object.
    Can be virtually anything. Key must be an int for the hash function to work as designed.
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
