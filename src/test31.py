import copy
import sys
board = [[0]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(4):
        board[i][j] = [data[j*2],data[j*2+1]-1]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def find(k,new_board):
    for i in range(4):
        for j in range(4):
            if new_board[i][j][0] == k:
                return [i,j]
    return None                

def turn_left(d):
    return (d+1) % 8

def move(x,y,new_board):
    for k in range(1,17):
        tmp = find(k,new_board)
        if tmp != None:
            pos_x, pos_y = tmp[0],tmp[1] 
            d = new_board[pos_x][pos_y][1] # 이동 방향
            for z in range(8):
                # pos에서 다른 8가지 방향을 확인하는 경우이므로 pos_x += dx[d]하면 값이 바뀌어 버리므로 안됨
                nx = pos_x + dx[d] 
                ny = pos_y + dy[d]
                if 0<=nx<4 and 0<=ny<4:
                    if not (nx == x and ny == y): # 상어가 아닌 경우
                        new_board[pos_x][pos_y][1] = d # 회전한 좌표로 갱신
                        new_board[pos_x][pos_y],new_board[nx][ny] = new_board[nx][ny],new_board[pos_x][pos_y]
                        break
                d = turn_left(d)

def possible(x,y,d,new_board):
    possible = []
    for k in range(4): 
        # 넘어온 좌표에서 계속 증가시켜가며 확인하고 싶은 경우
        # x좌표의 값을 바뀌어도 됨 # 4가지 방향이 아니라 4번 좌표를 바꿔가며 확인하는 것임
        x += dx[d] 
        y += dy[d]
        if 0<=x<4 and 0<=y<4:
            if new_board[x][y][0] != -1:
                possible.append([x,y])
    return possible

result = 0
def dfs(board,x,y,total):
    global result

    new_board = copy.deepcopy(board) # dfs수행할 때 마다 board복사해서 사용해야 함
    total += new_board[x][y][0]
    new_board[x][y][0] = -1
    shark_d = new_board[x][y][1]
    
    # new_board는 이 함수안에서만 있으므로 같이 넘겨줘야 함
    move(x,y,new_board) # 이동, 상어의 좌표같이 넘겨 줌
    possible_list = possible(x,y,shark_d,new_board) # 가능한 리스트 뽑기
    
    if possible_list == []:
        result = max(result,total)
        return
    else:
        for next_x,nexy_y in possible_list:
            dfs(new_board,next_x,nexy_y,total)
            
dfs(board,0,0,0)    
print(result)

