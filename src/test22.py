import sys

def move():
    tmp = [[0]*C for _ in range(R)] # 바뀐 board 리턴용
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0: # 이전 보드의 상어가 있으면
                x,y,s,d,z = i,j,board[i][j][0],board[i][j][1],board[i][j][2]
                while s>0: # 속도만큼 이동
                    x += dx[d] 
                    y += dy[d]
                    if 0<=x<R and 0<=y<C: # 범위안에 있는 경우
                        s-=1
                    else: # 범위 벗어난 경우
                        # 위에 증가시켜준 값을 감소시킴
                        x -= dx[d] 
                        y -= dy[d]    
                        # 방향 바꿔주기
                        if d == 0 or d == 2: 
                            d = d+1
                        elif d == 1 or d == 3:
                            d = d-1                            
                if tmp[x][y] == 0: # 최종으로 이동한 좌표가 빈칸이면
                    tmp[x][y] = [board[i][j][0],d,z] # 갱신
                else: # 이동한 좌표의 다른 상어가 있는 경우
                    if tmp[x][y][2] < z: # 원래 저장된 상어의 크기보다 지금 이동한 상어가 더 크기가 큰 경우
                        tmp[x][y] = [board[i][j][0],d,z] # 현재 상어로 갱신시킴
    return tmp                        

R,C,m = map(int,sys.stdin.readline().rstrip().split())

board = [[0]*C for _ in range(R)]
for i in range(m):
    r,c,s,d,z = map(int,input().split())
    board[r-1][c-1] = [s,d-1,z] # 속도,방향,크기 저장

dx = [-1,1,0,0]
dy = [0,0,1,-1]

answer = 0
for j in range(C):
    for i in range(R):
        if board[i][j] != 0: # 상어가 있으면
            answer += board[i][j][2] # 상어잡고
            board[i][j] = 0 # 빈칸만들기
            break # 하나만 잡기
    board = move() # 이동한 값으로 board 갱신   
print(answer)
