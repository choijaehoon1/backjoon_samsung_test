from collections import deque
import sys

def move(x,y):
    dist = [[-1]*N for _ in range(N)]
    dist[x][y] = 0
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if dist[nx][ny] == -1 and board[nx][ny] != -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
    # print(dist)       
    short = []             
    for i in range(N):
        for j in range(N):
            if board[i][j] != -1 and board[i][j] != 0:
                # print(board[i][j])
                for b in board[i][j]:
                    if b[0] == 0:
                        short.append([dist[i][j],i,j,b[1]])                            
                 
    if short == []:
        return None
    else:
        short.sort(key = lambda x:(x[0],x[1],x[2]))
        if short[0][0] == -1:
            return False           
        return short[0]

def d_move(x,y,num):
    dist = [[-1]*N for _ in range(N)]
    dist[x][y] = 0
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if dist[nx][ny] == -1 and board[nx][ny] != -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
    # print(dist)       
    short = []             
    for i in range(N):
        for j in range(N):
            if board[i][j] != -1 and board[i][j] != 0:
                for b in board[i][j]:
                    if b[1] == num and b[0] == 1:
                        short.append([dist[i][j],i,j])
                        break

    if short == []:
        return False
    else:
        if short[0] == -1:
            return False
        return short[0]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M,T = map(int,sys.stdin.readline().rstrip().split())
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))
    for j in range(N):
        if board[i][j] == 1:
            board[i][j] = -1

x,y = map(int,sys.stdin.readline().rstrip().split())

for i in range(M):
    s_x,s_y,d_x,d_y = map(int,sys.stdin.readline().rstrip().split())
    if board[s_x-1][s_y-1] == 0:
        board[s_x-1][s_y-1] = [[0,i+1]]
    if board[d_x-1][d_y-1] == 0:        
        board[d_x-1][d_y-1] = [[1,i+1]]
    if board[s_x-1][s_y-1] != -1 and board[s_x-1][s_y-1] != 0:        
        board[s_x-1][s_y-1].append([0,i+1]) 
    if board[d_x-1][d_y-1] != -1 and board[d_x-1][d_y-1] != 0:                
        board[d_x-1][d_y-1].append([1,i+1]) 

flag = False
while True:
    s = move(x-1,y-1)
    if s == None:
        break
    if s == False:
        flag = True
        break
        
    if s[0] > T:
        flag = True
        break
    tmp,x,y,num = s[0],s[1],s[2],s[3]    

    if len(board[x][y]) == 1:
        board[x][y] = 0
    elif len(board[x][y]) > 1:    
        board[x][y] = [i for i in board[x][y] if i != [0,num]]

    T -= tmp
    c = d_move(x,y,num)
    if c == False:
        flag = True
        break
    cost,d_x,d_y = c
    if len(board[d_x][d_y]) == 1:
        board[d_x][d_y] = 0
    elif len(board[d_x][d_y]) > 1:        
        board[d_x][d_y] = [i for i in board[d_x][d_y] if i != [1,num]]

    if cost > T:
        flag = True
        break
    T -= cost
    T = T + 2*(cost)
    x,y = d_x+1,d_y+1

if flag == True:
    print(-1)
else:    
    print(T)

