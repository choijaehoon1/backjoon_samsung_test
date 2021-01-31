import sys
n = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().rstrip().split()))
add,sub,mal,div = map(int,sys.stdin.readline().rstrip().split())

min_value = int(1e9)
max_value = -int(1e9)
def dfs(num,cnt):
    # min_value,max_value는 그때 그떄 dfs에 따라 최대 최소 값을 지정하기 위해 global 키워드 필요
    # add,sub,mal,div 역시 
    # 파이썬은 전역변수를 읽을 수는 있지만 수정하기 위해서는 global키워드 필요
    # list는 mutable, 튜플,숫자, 문자열 등의 변수도 모두 immutable
    # 따라서 일반적인 dfs문제에서 전역보드를 값 변경하는데 global키워드 필요없으나
    # 변수 같은 immutable은 global키워드 필요함
    global add,sub,mal,div,min_value,max_value
    if cnt == n:
        max_value = max(max_value,num)
        min_value = min(min_value,num)
        return

    if add > 0:
        add -= 1
        dfs(num+data[cnt] ,cnt+1)
        add += 1

    if sub > 0:
        sub -= 1
        dfs(num-data[cnt] ,cnt+1)
        sub += 1

    if mal > 0:
        mal -= 1
        dfs(num*data[cnt] ,cnt+1)
        mal += 1

    if div > 0:
        div -= 1
        dfs(int(num/data[cnt]),cnt+1)
        div += 1        

dfs(data[0],1)
print(max_value)
print(min_value)
