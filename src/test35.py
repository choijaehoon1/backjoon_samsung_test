import sys

def move(x,y,m,s,d):
    nx = (x + s*dx[d]) % N 
    ny = (y + s*dy[d]) % N 
    board[nx-1][ny-1].append([nx,ny,m,s,d])
    board[x-1][y-1].remove([x,y,m,s,d])


def divide(tmp_list):
    sum_m = 0
    sum_s = 0
    sum_d = 0
    d_list = []
    cnt = len(tmp_list)
    for tmp in tmp_list:
        r,c,m,s,d = tmp
        sum_m += m
        sum_s += s
        if d % 2 == 1:
            d_list.append(False)
        else:
            d_list.append(True)                        

    for i in tmp_list:
        board[i[0]-1][i[1]-1] = []
        new_r,new_c = i[0], i[1]
        break
    new_m = sum_m // 5            
    new_s = sum_s // cnt

    check = d_list[0]
    flag = True
    for i in range(1,len(d_list)):
        if check != d_list[i]:
            flag = False
            break
    
    if new_m != 0:
        if flag == True:
            for k in range(0,8,2):
                board[new_r-1][new_c-1].append([new_r,new_c,new_m,new_s,k])
                fire_ball.append([new_r,new_c,new_m,new_s,k])
        elif flag == False:
            for k in range(1,8,2):
                board[new_r-1][new_c-1].append([new_r,new_c,new_m,new_s,k])
                fire_ball.append([new_r,new_c,new_m,new_s,k])


N,M,K = map(int,sys.stdin.readline().rstrip().split())
board = [[[] for _ in range(N)] for _ in range(N)]
fire_ball = []
for i in range(M):
    r,c,m,s,d = map(int,sys.stdin.readline().rstrip().split())
    board[r-1][c-1].append([r,c,m,s,d])
    fire_ball.append([r,c,m,s,d])

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
for _ in range(K):
    for f in fire_ball:
        r,c,m,s,d = f
        move(r,c,m,s,d)
    
    fire_ball = []        
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                # print(board[i][j])
                divide(board[i][j])
            elif len(board[i][j]) == 1: 
                for f in board[i][j]:
                    fire_ball.append(f)
    
result = 0
for i in range(N):
    for j in range(N):
        if board[i][j] != []:
            for k in board[i][j]:
                result += k[2]
print(result)


