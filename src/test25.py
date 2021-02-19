import sys

def process(x,y,d1,d2):
    calcu = [0 for _ in range(6)] # 각 구역의 합 저장리스트
    tmp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(d1+1): # 경계선 1,4
        tmp[x+i][y-i] = 5
        tmp[x+d2+i][y+d2-i] = 5

    for i in range(d2+1): # 경계선 2,3
        tmp[x+i][y+i] = 5        
        tmp[x+d1+i][y-d1+i] = 5
    # 안쪽의 5구역 채우기
    for i in range(x+1,x+d1+d2): # x+1번째행부터 마지막 해당되는 행 위까지 확인
        flag = False
        for j in range(1,n+1): # 열에 대해 확인
            if tmp[i][j] == 5:
                flag = not flag # 플래그 토글
            if flag == True:
                tmp[i][j] = 5
                
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i < x+d1 and j <= y and tmp[i][j] == 0:
                calcu[1] += board[i][j]
            elif i <= x+d2 and y < j and tmp[i][j] == 0:
                calcu[2] += board[i][j]
            elif x+d1 <= i and j < y-d1+d2 and tmp[i][j] == 0:
                calcu[3] += board[i][j]                
            elif x+d2 < i and y-d1+d2 <= j and tmp[i][j] == 0:
                calcu[4] += board[i][j]                    
            elif tmp[i][j] == 5:
                calcu[5] += board[i][j]

    num = max(calcu[1:]) - min(calcu[1:]) # 최대 - 최소 리턴
    return num

n = int(sys.stdin.readline().rstrip())
board = [[]] # 1,1 부터 표현하기 위해 변환
for i in range(n):
    board.append([0]+list(map(int,sys.stdin.readline().rstrip().split()))) # 1,1 부터 표현하기 위해 변환

answer = int(1e9)
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                # 주어진 조건에 만족하면 process함수 수행
                if 1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <= n:
                    num = process(x,y,d1,d2)
                    answer = min(answer, num)
print(answer)                    

