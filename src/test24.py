from collections import deque
from itertools import combinations
import sys

def bfs():
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n:
                # 방문하지 않았고 벽이 아닌 경우
                if visit[nx][ny] == 0 and board[nx][ny] != 1:
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y]+1
                    q.append([nx,ny])

n,m = map(int,sys.stdin.readline().rstrip().split())
board = []
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]    

INF = int(1e9)
virus = []
check = 0 # 바이러스가 활성화될 칸의 개수
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append([i,j]) # 튜플형태로 넣을 때에는 주의 필요           
        if board[i][j] != 1:
            check += 1
        
answer = INF
for combi in combinations(virus,m):
    # 동시에 퍼져나가게 하기위해 q에 바이러스 정보를 넣고 bfs 수행
    # 최단거리 테이블도 만들어 같이 수행
    q = deque()
    dist = [[-1]*n for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    for x,y in combi:
        q.append([x,y])
        dist[x][y] = 0
        visit[x][y] = 1
    bfs()        
    # 방문한 칸 카운팅
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 1:
                cnt += 1
    # 바이러스를 확산시킬 수 있는 경우          
    if cnt == check:
        max_num = 0 # 주의 -INF로 하지 말것
        for j in range(n):
            for k in range(n):
                if board[j][k] != 1 and [j,k] not in virus: # 벽이아닌 칸이고 바이러스 시작칸이 아닌 경우 check
                    max_num = max(max_num,dist[j][k]) # 가장 마지막 확산시칸 저장
        answer = min(answer,max_num) # combinations 중 가장 작은 값 저장

if answer == INF: 
    print(-1)
else:
    print(answer)    
