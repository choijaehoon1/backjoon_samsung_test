import copy
n,m = map(int,input().split())
board = []
cctv_list = []
cctv_cnt = 0
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(m):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv_list.append((i,j,board[i][j]))
            cctv_cnt += 1
# 북 서 남 동 (시계방향으로 지정)
dx = [-1,0,1,0]
dy = [0,1,0,-1]            
# 각각 이동할 수 있는 방향리스트 선언(북:0이라 가정)      
direction = [[],[[0],[1],[2],[3]], [[3,1],[0,2]],[[0,1],[1,2],[2,3],[3,0]],[[3,0,1],[0,1,2],[1,2,3],[2,3,0]],[[0,1,2,3]]]
answer = int(1e9)

def bfs(board,x,y,direction): # tmp_board의 값이 바뀌는 것임
    for i in direction: # 각각의 방향마다 check
        nx,ny = x,y # nx,ny는 각각의 방향마다 bfs수행할때 넘어온 x,y로 갱신해줘야 함
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 6:
                    break
                elif board[nx][ny] == 0:
                    board[nx][ny] = "#"
            else:
                break

def get_sum(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt+=1
    return cnt

def dfs(board,cnt):
    global answer
    # cctv 검사 다하면 최소값 갱신
    if cnt == cctv_cnt:
        answer = min(answer, get_sum(board))
        return

    tmp_board = copy.deepcopy(board) # dfs타고 들어온 board 복사해서 사용
    x,y,num = cctv_list[cnt]
    for i in direction[num]: # 해당 cctv가 볼수 있는 방향탐색
        bfs(tmp_board,x,y,i) # tmp_board를 변화시키고
        dfs(tmp_board,cnt+1) # tmp_board로 dfs 수행
        tmp_board = copy.deepcopy(board) # 같은 번호의 다른 방향check하기 위해 값바뀌기 전 board복사하여 갱신

dfs(board,0)
print(answer)
