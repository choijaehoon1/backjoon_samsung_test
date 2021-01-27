from collections import deque
n = int(input())
k = int(input())

board = [[0]*(n+1) for _ in range(n+1)]

for i in range(k):
    a,b = map(int,input().split())
    board[a][b] = 1

data = []    
l = int(input())
for i in range(l):
    a,b = input().split()
    data.append((int(a),b))

# 동쪽부터 시계방향
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 초기 setting
x,y = 1,1    
board[x][y] = 2
direction = 0
time = 0
idx = 0
# 뱀의 길이
q = deque()
q.append([x,y])

def turn(direction,c):
    if c == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4        
    return direction

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 1<=nx<=n and 1<=ny<=n and board[nx][ny] != 2:
        if board[nx][ny] == 0: # 아무것도 없는 경우
            board[nx][ny] = 2
            q.append([nx,ny])
            px,py = q.popleft()
            board[px][py] = 0
        if board[nx][ny] == 1: # 사과먹은 경우 뱀 길이 증가
            board[nx][ny] = 2
            q.append([nx,ny])
    else: # 벽에 부딪히거나 자기자신에 닿은 경우
        time += 1
        break
    
    x,y = nx,ny # 갱신
    time += 1
    # idx 증가 시키는데 주어진 l보다 작은 경우를 먼저 검사해야함
    # time이 증가하면서 비교하다가 어느 순간 idx증가하여 리스트 범우 벗어날 수 있음
    if idx < l and time == data[idx][0]:
        direction = turn(direction,data[idx][1])
        idx += 1    
print(time)

