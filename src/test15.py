import sys
n,m,h = map(int,sys.stdin.readline().rstrip().split())

INF = int(1e9)
# h가 가로선마다 놓을 수 있는 개수이므로 행을 h로 잡음
board = [[0]*(n+1) for _ in range(h+1)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    board[a][b] = 1 # b와 b+1 세로선연결하는 행은 a

def check():
    # 현재 열에 대해 수행했을때 마지막에 도착한 열이 같은지 확인
    for i in range(1,n+1):
        tmp = i
        for j in range(1,h+1):
            if board[j][tmp] == 1:
                tmp += 1
            elif board[j][tmp-1] == 1:
                tmp -= 1    
        if i != tmp:
            return False
    return True

def dfs(latter_cnt,current_cnt):
    global result
    if result != INF: # result 값이 바뀌엇으면 리턴
        return
    if latter_cnt == current_cnt: # 현재 새로운 사다리 세웠을때 확인
        if check(): # check가 True인 경우만 값변화
            result = current_cnt
        return # 리턴은 check가 false여도 해줘야하므로 여기서 리턴

    for j in range(1,n): # 열에 대해서 확인
        for i in range(1,h+1): # 행에 대해서 확인
            # 양옆에 연결 안되어있고 현재 값도 0일때 사다리 세워보기
            if board[i][j-1] == 0 and board[i][j+1] == 0 and board[i][j] == 0: 
                board[i][j] = 1
                dfs(latter_cnt,current_cnt+1)
                board[i][j] = 0 # 복구
                # 행의 양옆중 하나가 연결되어 있으면 바로 그다음 경우 확인하로 break하나 
                # 그렇지 않다면 행을 증가시켜 확인 후 이동할수 있는 행을 찾는 과정
                while i<h: 
                    if board[i][j-1] == 1 or board[i][j+1] == 1:
                        break
                    i+=1

result = INF 
for i in range(4): # 완전탐색(0개,1개,2개,3개) 높을 수 있으므로 각각 dfs 수행
    dfs(i,0) # 다리놓는개수, 현재 개수
    if result != INF: # result값이 바뀌었다는 건 check() 함수 True여서 값변화된 것이므로 가능한 경우임
        print(result)
        break
# 끝까지 수행했는데 result 변화없으면 불가능한 경우
if result == INF:
    print(-1)    
    
