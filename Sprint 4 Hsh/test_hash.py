def test(): 
    o_one = myhashtable()

    o_one.put(key = 1, value = 14)
    print(o_one.buckets[:5])
    o_one.put(key = 1001, value = 24)
    print(o_one.buckets[:5])
    o_one.put(key = 1002, value = 0)
    print(o_one.buckets[:5])
    o_one.put(key = 1003, value = 1414)
    print(o_one.buckets[:5])
    o_one.put(key = 1, value = 25)
    print(o_one.buckets[:5])
    o_one.put(key = 1001, value = 25)
    print(o_one.buckets[:5])
    print('\nget\n')
    print(o_one.get(1))
    print(o_one.get(1001))
    print(o_one.get(12))
    print(o_one.get(3001))
    print('\ndeletion\n')
    print(o_one.delete(5))
    print(o_one.buckets[:5])
    print(o_one.delete(1))
    print(o_one.buckets[:5])
    print(o_one.delete(1002))
    print(o_one.buckets[:5])
    print(o_one.delete(1001))
    print(o_one.buckets[:5])
