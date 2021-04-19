import sys
n,m = map(int,input().split())
r,c,d = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

# 북,동,남,서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left(direction):
    return (direction -1) % 4

def get_sum():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                cnt +=1
    return cnt                

def move(x,y,direction,turn_count):
    while True:
        if turn_count == 4: # 4방향 다 검새 했으면 1칸후진해서 확인
            back_x = x - dx[direction]
            back_y = y - dy[direction]
            if board[back_x][back_y] == 1: # 벽이면 종료
                print(get_sum())
                return
            else: # 벽이 아니면 해당 좌표로 다시 수행
                x,y,direction,turn_count = back_x,back_y,direction,0    
        # 현재 위치 청소
        if board[x][y] == 0:
            board[x][y] = 2
        
        # 왼쪽으로 회전(주어진 조건이 왼쪽방향부터 차례대로 검사한다고 주어짐)
        new_direction = turn_left(direction)
        nx = x + dx[new_direction] # 왼쪽 회전 후 x좌표
        ny = y + dy[new_direction] # 왼쪽 회전 후 y좌표

        if board[nx][ny] == 0: # 이동할 위치가 아직 청소안된 경우
            x,y,direction,turn_count = nx,ny,new_direction,0
        else: # 이미 청소했거나 벽인 경우(값이 2이거나 1) 좌표변경안하고 회전 count만 증가
            x,y,direction,turn_count = x,y,new_direction,turn_count + 1                        

move(r,c,d,0)
