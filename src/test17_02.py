from itertools import combinations
n,m = map(int,input().split())

house = []
chicken = []
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1: 
            house.append((r,c)) 
        elif data[c] == 2: 
            chicken.append((r,c)) 

def short_distance(candidate):
    result = 0
    for hx,hy in house:
        tmp = 1e9 
        for cx,cy in candidate:
            tmp = min(tmp,abs(hx-cx) + abs(hy-cy))
        result += tmp     
    return result

candidates = list(combinations(chicken,m))

result = 1e9
for candidate in candidates:
    result = min(result,short_distance(candidate))
print(result)
