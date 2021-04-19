import sys

def smell_update():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if board[i][j] != 0:
                smell[i][j] = [board[i][j],k]    

def move():
    new_board = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if board[x][y] != 0:
                direction = direction_list[board[x][y]-1]
                found = False
                for k in range(4):
                    nx = x + dx[priorities[board[x][y]-1][direction-1][k]-1]
                    ny = y + dy[priorities[board[x][y]-1][direction-1][k]-1]
                    if 0<=nx<n and 0<=ny<n:
                        if smell[nx][ny][1] == 0:
                            direction_list[board[x][y]-1] = priorities[board[x][y]-1][direction-1][k]

                            if new_board[nx][ny] == 0:
                                new_board[nx][ny] = board[x][y]
                            else:
                                new_board[nx][ny] = min(new_board[nx][ny],board[x][y])
                            found = True
                            break
                if found:
                    continue
                
                for k in range(4):
                    nx = x + dx[priorities[board[x][y]-1][direction-1][k]-1]
                    ny = y + dy[priorities[board[x][y]-1][direction-1][k]-1]
                    if 0<=nx<n and 0<=ny<n:
                        if smell[nx][ny][0] == board[x][y]:
                            direction_list[board[x][y]-1] = priorities[board[x][y]-1][direction-1][k]
                            new_board[nx][ny] = board[x][y]
                            break

    return new_board

n,m,k = map(int,input().split())
board = []
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

direction_list = list(map(int,sys.stdin.readline().rstrip().split()))

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int,sys.stdin.readline().rstrip().split())))

smell = [[[0,0]]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]      

time = 0
while True:
    smell_update()    
    new_board = move()
    board = new_board
    time += 1

    flag = True
    for i in range(n):
        for j in range(n):
            if board[i][j] > 1:
                flag = False
    if flag:
        print(time)                
        break

    if time >= 1000:
        print(-1)
        break
