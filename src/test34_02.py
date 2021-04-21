import sys

def move(x,y,array):
    new_board = [[0]*N for _ in range(2)]                 
    cx,cy = x,y
    for k in range(4):
        while True:
            nx = x + dx[k]
            ny = y + dy[k]
            if nx == cx and ny == cy:
                new_board[nx][ny] = array[x][y]
                return new_board
            if 0<=nx<2 and 0<=ny<N:
                new_board[nx][ny] = array[x][y]
            else:
                break
            x,y = nx,ny                                

N,K = map(int,sys.stdin.readline().rstrip().split())
tmp = list(map(int,sys.stdin.readline().rstrip().split()))
belt = []
belt.append(tmp[:N])
belt.append(list(reversed(tmp[N:])))
robot = [[0]*N for _ in range(2)] 

robot_list = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

step = 1
tmp = 1
while True:
    belt = move(0,0,belt)
    robot = move(0,0,robot)
    
    robot_list = []
    for i in range(2):
        for j in range(N):
            if i == 0 and j == N-1 and robot[i][j] != 0:
                robot[i][j] = 0
            if robot[i][j] != 0:
                robot_list.append([i,j,robot[i][j]])
    
    robot_list.sort(key = lambda x:x[2])
    for robo in robot_list[:]:
        x,y,s = robo
        if x == 0 and y == N-2 and belt[x][y+1] >= 1:
            robot[x][y] = 0
            belt[x][y+1] -= 1

        if x == 0 and y < N-2 and robot[x][y+1] == 0 and belt[x][y+1] >= 1:
            robot[x][y] = 0      
            robot[x][y+1] = s
            belt[x][y+1] -= 1
            robot_list.append([x,y+1,s])
            robot_list.remove([x,y,s])
    
    if robot[0][0] == 0 and belt[0][0] >=1:
        robot[0][0] = tmp
        belt[0][0] -= 1
        robot_list.append([0,0,tmp])
        tmp += 1
    
    cnt = 0
    for i in range(2):
        cnt += belt[i].count(0)
    if cnt >= K:
        print(step)
        break  
    step += 1 
    
