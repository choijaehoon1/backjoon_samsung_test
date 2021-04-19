import sys
n,m,x,y,k = map(int,sys.stdin.readline().rstrip().split())

board = []
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))
data = list(map(int,sys.stdin.readline().rstrip().split()))

dice = [0 for _ in range(7)]
# 동,서,북,남
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in data:
    direction = i-1
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0<=nx<n and 0<=ny<m:
        if i == 1: # 동
            dice[1],dice[3],dice[4],dice[6] = dice[3],dice[6],dice[1],dice[4]
        elif i == 2: # 서
            dice[1],dice[3],dice[4],dice[6] = dice[4],dice[1],dice[6],dice[3]
        elif i == 3: # 북
            dice[1],dice[2],dice[5],dice[6] = dice[2],dice[6],dice[1],dice[5]            
        elif i == 4: # 남
            dice[1],dice[2],dice[5],dice[6] = dice[5],dice[1],dice[6],dice[2]                        
    else: # 범위안에 없으면 출력을 하지 말라는 조건이 있으므로 처리
        continue

    if board[nx][ny] == 0:
        board[nx][ny] = dice[1] # dice[1] 밑면(아래)
    else:
        dice[1] = board[nx][ny]
        board[nx][ny] = 0
    x,y = nx,ny        
    print(dice[6]) # 하늘보고 있는 면
