from collections import deque
import sys
n,m = map(int,sys.stdin.readline().rstrip().split())

board = []
for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if board[i][j] == 'R':
            red_x, red_y = i,j
        if board[i][j] == 'B':           
            blue_x,blue_y = i,j

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visit = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def move(x,y,dx,dy):
    cnt = 0
    # 구슬을 중력에 따라 이동시킴(이동시킬 위치가 벽이고 구멍이 아니어야함)
    # 예를들어 다음칸이 벽은 아니지만 지금 위치가 구멍이면 더이상 수행안함
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x,y,cnt

def bfs(red_x,red_y,blue_x,blue_y,cnt):
    # 초기작업
    q = deque()
    q.append([red_x,red_y,blue_x,blue_y,cnt])
    visit[red_x][red_y][blue_x][blue_y] = 1

    while q:
        red_x,red_y,blue_x,blue_y,cnt = q.popleft()
        if cnt > 10:
            return -1
        
        for k in range(4):
            # 4방향에 따라 빨간색,파란색 구슬을 이동시킴
            nrx,nry,r_cnt = move(red_x,red_y,dx[k],dy[k])
            nbx,nby,b_cnt = move(blue_x,blue_y,dx[k],dy[k])
            
            if board[nbx][nby] != 'O': # 파란색이 들어가면 안됨
                if board[nrx][nry] == 'O': # 빨간색이 들어가면 종료
                    return cnt   
                # 겹치면 안되므로 같은 좌표일때 더 많이 이동한 구슬을 한칸 이전 값으로 변경
                if nrx == nbx and nry == nby: 
                    if r_cnt > b_cnt:
                        nrx -= dx[k]
                        nry -= dy[k]
                    else:    
                        nbx -= dx[k]
                        nby -= dy[k]
                # 최종적으로 구슬을 배치했을 때 방문하지 않은 것일때                        
                if visit[nrx][nry][nbx][nby] == 0:
                    visit[nrx][nry][nbx][nby] = 1
                    q.append([nrx,nry,nbx,nby,cnt+1])
    return -1 # 파란색이 구멍에 들어가면 -1
result = bfs(red_x,red_y,blue_x,blue_y,1)
print(result)

