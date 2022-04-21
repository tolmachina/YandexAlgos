def remained_candies(kids, candies):
    total_candy = 0
    for c in candies:
        total_candy += c
    
    if total_candy >= kids:
        return total_candy % kids 
    else:
        return 0


t = int(input())
for i in range(t):
    nm = list(map(int, input().split()))# candy bags
    kids = nm[1]
    candies = list(map(int, input().split()))
    print(f"Case #{i}: {remained_candies(kids, candies)}")

