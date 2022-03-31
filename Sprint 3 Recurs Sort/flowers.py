def overlap( a, b):
        return a[0] <= b[1] and b[0] <= a[1]
        
def flower_beds(arr):
    arr.sort(key=lambda x : x[0])

    merged = []
    for pair in arr:
        if not merged or not overlap(a = merged[-1], b = pair):
            merged.append(pair)
        else:
            if overlap(a = merged[-1],b = pair):
                merged[-1][1] = max (merged[-1][1], pair[1])
    return merged

def inp_data():
    n = int(input())
    segments =[None] * n
    for i in range(n):
        segment = list(map(int, input().split()))
        segments[i] = segment
    return segments

def test_flower_beds():
    x = [[7,8],[7,8],[2,3],[6,10]]
    y = [[2,3],[5,6],[3,4],[3,4]]
    z = [[1,3],[3,5],[4,6],[5,6],[2,4],[7,10]]
    print(
    flower_beds(x),"\n",
    flower_beds(y),"\n",
    flower_beds(z),"\n",
    )


merged = flower_beds(inp_data())

for flower in merged:
    print(*flower)