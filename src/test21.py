def spread(x,y,num):
    cnt = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<r and 0<=ny<c and new_board[nx][ny] != -1:
            cnt += 1
            new_board[nx][ny] += num
    return cnt         

def clean(x,y,dirs):
    tmp = copy.deepcopy(new_board) # board상태를 tmp에 저장
    cx,cy = x,y-1 # 종료조건(넘길때 +1 해서 넘겼으므로 조정)
    new_board[x][y] = 0 # y좌표 +1의 값은 0으로 설정
    for k in range(4): # 4방향 수행
        while True:
            nx = x + dx[dirs[k]]
            ny = y + dy[dirs[k]]
            if nx == cx and ny == cy: # 종료
                return
            if 0<=nx<r and 0<=ny<c: # 범위안에 있으면 값 갱신
                new_board[nx][ny] = tmp[x][y]
            else: # 범위벗어나면 다른 방향으로 수행
                break
            x,y = nx,ny # 좌표 갱신

from collections import deque
import copy
import sys
r,c,t = map(int,sys.stdin.readline().rstrip().split())

board = []
for i in range(r):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(t):
    new_board = [[0]*c for _ in range(r)] 
    dust = deque()
    clear = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == -1:
                clear.append((i,j))
                new_board[i][j] = board[i][j]
            if board[i][j] != -1 and board[i][j] != 0:
                dust.append((i,j))
                new_board[i][j] = board[i][j]
    # 확산시키기
    for _ in range(len(dust)):
        x,y = dust.popleft()
        num = board[x][y]//5 
        cnt = spread(x,y,num) # 퍼진 방향만큼 빼주는 용도
        new_board[x][y] -= (cnt*num)
    # print(new_board)
    clean(clear[0][0],clear[0][1]+1,[3,0,2,1]) # 시계반대방향
    clean(clear[1][0],clear[1][1]+1,[3,1,2,0]) # 시계방향
    # print(new_board)    

    board = copy.deepcopy(new_board) # 갱신
    
answer = 0
for i in range(r):
    answer += sum(board[i]) 
print(answer+2) # -1포함되어있으므로 2 증가   

