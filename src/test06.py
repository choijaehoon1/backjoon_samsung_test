n = int(input())
dp = [0 for _ in range(n+1)] 

data = []
for i in range(n):
    data.append(list(map(int,input().split())))

for i in range(len(data)-1,-1,-1): # data의 인덱스는 0~6임
    time = i + data[i][0] # 현재 수행하는 시간
    if time < n+1: # 시간안에 가능한 경우
        dp[i] = max(dp[time] + data[i][1],dp[i+1]) # 그때 시간의 dp + 금액과 이미 구해졌던 dp 중 최대값
    else: # 범위벗어나면 뒤에 값 복사
        dp[i] = dp[i+1]        
print(dp[0]) # 제일 앞의 값 출력
