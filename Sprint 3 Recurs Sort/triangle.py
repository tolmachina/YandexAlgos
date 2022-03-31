def inp_data():
    n = input()
    lenghts = list(map(int, input().split()))
    return lenghts

def algosses(lenghts):
    lenghts.sort()
    sides = []

    while lenghts:
        c = lenghts[-1]
        b = lenghts[-2]
        a = lenghts[-3]
        if c < (a + b):
            return a + b + c
        else:
            lenghts.pop()

lenghts = inp_data()

print(algosses(lenghts))