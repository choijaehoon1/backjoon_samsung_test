from collections import deque
import sys

def check(nx,ny):
    if len(chess_board[nx][ny]) >= 4: # 
        return True
    return False        

def white(x,y,nx,ny):
    first = chess_board[x][y].index(j) # j는 for문에서 체스의 진행중인 현재 번호
    last = len(chess_board[x][y]) # 위에 올려지는 모든 말은 같이 이동
    
    # 시작 체스부터 그 위에 있는 말까지 조정
    for k in range(first,last): # 체스 번호 인덱스
        # chess_board[x][y][k]는 해당 체스 좌표에 있는 체스 번호
        chess[chess_board[x][y][k]][0] = nx 
        chess[chess_board[x][y][k]][1] = ny
        chess_board[nx][ny].append(chess_board[x][y][k]) # 새로운 체스판 좌표에 체스의 번호를 더해줌

    # 원래 체스보드의 좌표에 있는 말들 제거
    for _ in range(first,last):
        chess_board[x][y].pop()

def red(x,y,nx,ny):
    first = chess_board[x][y].index(j) # j는 for문에서 체스의 진행중인 현재 번호
    last = len(chess_board[x][y]) # 위에 올려지는 모든 말은 같이 이동
    
    for k in range(last-1,first-1,-1): # 빨간색 칸은 뒤집어서 체스 좌표 설정해야함
        chess[chess_board[x][y][k]][0] = nx # 체스 위치 변경
        chess[chess_board[x][y][k]][1] = ny
        chess_board[nx][ny].append(chess_board[x][y][k]) # 새로운 체스판 좌표에 체스의 번호를 더해줌

    # 원래 체스보드의 좌표에 있는 말들 제거
    for _ in range(first,last):
        chess_board[x][y].pop()        

n,k = map(int,sys.stdin.readline().rstrip().split())

board = [] # 흰색, 빨강, 파랑 보드
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))
chess_board = [[deque() for _ in range(n)] for _ in range(n)] # 체스보드
chess = [] # 체스 좌표와 방향저장 리스트
for i in range(k):
    r,c,d = map(int,sys.stdin.readline().rstrip().split())
    chess_board[r-1][c-1].append(i) # 체스 번호 0부터 시작한다고 가정
    chess.append([r-1,c-1,d-1]) # x,y,방향정보

dx = [0,0,-1,1]
dy = [1,-1,0,0] 

for i in range(1,1001):
    for j in range(k): # chess리스트는 0부터 시작이므로
        x,y,d = chess[j] # 체스 하나씩 확인
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0: # 흰색인 경우
            white(x,y,nx,ny) 
            if check(nx,ny) == True: # 좌표에 말이 4개이상인 경우 종료
                print(i)
                exit()
        elif 0<=nx<n and 0<=ny<n and board[nx][ny] == 1: # 빨간색 칸의 경우
            red(x,y,nx,ny)
            if check(nx,ny) == True:
                print(i)
                exit()
        elif not (0<=nx<n and 0<=ny<n) or board[nx][ny] == 2: # 범위 벗어나거나 파란색 칸의 경우
            # 방향전환
            if d == 0: d = 1
            elif d ==1: d = 0
            elif d ==2: d = 3
            elif d ==3: d = 2

            chess[j][2] = d # 해당 체스 방향 변경
            nx = x + dx[d]
            ny = y + dy[d]
            # 파란색인 경우는 그대로 멈추게 됨
            # 방향 변경 저장 후 이동활 좌표가 흰색인 경우
            if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                white(x,y,nx,ny)
                if check(nx,ny) == True:
                    print(i)
                    exit()
            # 방향 변경 저장 후 이동활 좌표가 빨간색인 경우                    
            elif 0<=nx<n and 0<=ny<n and board[nx][ny] == 1:
                red(x,y,nx,ny)
                if check(nx,ny) == True:
                    print(i)
                    exit()
else:
    print(-1)

