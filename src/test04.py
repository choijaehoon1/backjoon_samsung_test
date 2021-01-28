import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split())) 
b,c = map(int,sys.stdin.readline().rstrip().split())

result = 0
for i in data:
    i -= b
    num = 1
    if i > 0:
        if i <= c:
            num += 1
        else:
            res = i % c
            if res == 0:
                num += i//c
            else:        
                num += i//c + 1
    result += num                
print(result)
