from collections import deque
import copy
import sys

# 배열 한칸 돌리기
# def move(x,y,idx):
#     cx,cy = x,y
#     for k in range(4):
#         while True:
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if nx == cx and ny == cy:
#                 new_board[nx][ny] = board[x][y]
#                 return
#             if cx <= nx < cx+ idx and cy <= ny < cy+ idx:
#                 new_board[nx][ny] = board[x][y]
#             else:
#                 break
#             x,y = nx,ny                

def move(x,y,idx):
    tmp_board = [[0]*idx for _ in range(idx)]
    t_i = 0
    for i in range(x,x+idx):
        t_j = 0
        for j in range(y,y+idx):
            tmp_board[t_j][idx-1-t_i] = board[i][j]
            t_j +=1
        t_i += 1            
    
    t_i = 0
    for i in range(x,x+idx):
        t_j = 0
        for j in range(y,y+idx):
            new_board[i][j] = tmp_board[t_i][t_j]
            t_j +=1
        t_i += 1               


def check(x,y):
    cnt = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<2**N and 0<=ny<2**N:
            if new_board[nx][ny] >= 1:
                cnt +=1
    
    if cnt <= 2:    
        return True
    return False                        

def bfs(x,y):
    cnt = 1
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<2**N and 0<=ny<2**N:
                if visit[nx][ny] == 0 and board[nx][ny] != 0:
                    visit[nx][ny] = 1
                    q.append([nx,ny])
                    cnt += 1                             
    return cnt                    


N,Q = map(int,sys.stdin.readline().rstrip().split())
board = []
for i in range(2**N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

step = list(map(int,sys.stdin.readline().rstrip().split()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
new_board = [[0]*(2**N) for _ in range(2**N)]
for s in step:
    idx = 2**s
    
    for i in range(0,2**N,idx):
        for j in range(0,2**N,idx):
            move(i,j,idx)

    delete_list = []
    for i in range(2**N):
        for j in range(2**N):
            if check(i,j) == True and new_board[i][j] >= 1:
                delete_list.append([i,j])
    
    for x,y in delete_list:
        new_board[x][y] -= 1  
    
    board = copy.deepcopy(new_board)

visit = [[0]*(2**N) for _ in range(2**N)]
total = 0
num = 0
for i in range(2**N):
    for j in range(2**N):
        total += new_board[i][j]
        if visit[i][j] == 0 and new_board[i][j] != 0:
            tmp = bfs(i,j)
            num = max(num, tmp)

print(total)
print(num)

