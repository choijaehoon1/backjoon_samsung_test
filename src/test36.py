import sys

left = [
    [-2,0,0.02],[-1,-1,0.1],[-1,0,0.07],[-1,1,0.01],
    [2,0,0.02],[1,-1,0.1],[1,0,0.07],[1,1,0.01],
    [0,-2,0.05],[0,-1,0]
]

right = [
    [-2,0,0.02],[-1,-1,0.01],[-1,0,0.07],[-1,1,0.1],
    [2,0,0.02],[1,-1,0.01],[1,0,0.07],[1,1,0.1],
    [0,2,0.05],[0,1,0]
]

up = [
    [0,-2,0.02],[1,-1,0.01],[0,-1,0.07],[-1,1,0.1],
    [0,2,0.02],[1,1,0.01],[0,1,0.07],[-1,-1,0.1],
    [-2,0,0.05],[-1,0,0]
]

down = [
    [0,-2,0.02],[-1,-1,0.01],[0,-1,0.07],[1,1,0.1],
    [0,2,0.02],[-1,1,0.01],[0,1,0.07],[1,-1,0.1],
    [2,0,0.05],[1,0,0]
]


def move(d,cnt,k):
    global x,y
    for i in range(cnt): 
        nx = x + dx[k]
        ny = y + dy[k]
        x,y = nx,ny
        simul(x,y,d)
        if nx == 0 and ny == 0:
            return True

    return False              

def simul(x,y,d):
    global result
    if d == 'l':
        rate = left
    elif d == 'd':
        rate = down        
    elif d == 'r':
        rate = right
    elif d == 'u':
        rate = up

    tmp = 0
    for t_x,t_y,r in rate:
        nx = x + t_x
        ny = y + t_y
        if r == 0:
            num = board[x][y] - tmp
        else:
            num = int(board[x][y]*r)
        
        if 0<=nx<N and 0<=ny<N:
            board[nx][ny] += num
        else:
            result += num

        tmp += num

result = 0
N = int(sys.stdin.readline().rstrip())
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

x,y = N//2,N//2
dx = [0,1,0,-1]
dy = [-1,0,1,0]

flag = False
for i in range(N):
    if i % 2 == 0:
        flag = move('l',i+1,0)
        if flag:
            break
        flag = move('d',i+1,1)
    else:
        move('r',i+1,2)
        move('u',i+1,3)                
print(result)        
