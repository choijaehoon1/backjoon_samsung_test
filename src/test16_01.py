# 시간초과
from itertools import combinations
from collections import deque
import sys
n,m = map(int,sys.stdin.readline().rstrip().split())

board = []
chickens = []
homes = []
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if board[i][j] == 2:
            chickens.append((i,j))
            board[i][j] = 0
        if board[i][j] == 1:            
            homes.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(board,x,y):
    dist = [[-1]*n for _ in range(n)]
    dist[x][y] = 0
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx,ny])                
    return dist

result = int(1e9)
for chicken in combinations(chickens,m):
    # print(chicken)
    # 치킨
    for c_x,c_y in chicken:
        board[c_x][c_y] = 2
        
    answer = 0
    for h_x,h_y in homes:
        tmp_dist = bfs(board,h_x,h_y)
        tmp_num = int(1e9)
        for x,y in chicken:
            tmp_num = min(tmp_num,tmp_dist[x][y])
        answer += tmp_num

    result = min(result,answer)

    # 원복
    for c_x,c_y in chicken:
        board[c_x][c_y] = 0
print(result)        
