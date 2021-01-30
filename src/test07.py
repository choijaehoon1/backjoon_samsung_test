from collections import deque
n,m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
# bfs하기 위한 용도의 전역 보드
tmp_board = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append([x,y])    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and tmp_board[nx][ny] == 0:
                tmp_board[nx][ny] = 2
                q.append([nx,ny])

def get_score(array):
    answer = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                answer += 1
    return answer                

def dfs(cnt):
    global result
    if cnt == 3:
        # bfs해서 구하기 위해 tmp_board 사용, 이전 보드 그대로 사용시 dfs할때 문제생기므로
        for i in range(n):
            for j in range(m):
                tmp_board[i][j] = board[i][j]

        for i in range(n):
            for j in range(m):
                if tmp_board[i][j] == 2:
                    bfs(i,j)
        answer = get_score(tmp_board)
        result = max(result,answer)
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0: # 전역보드
                board[i][j] = 1
                cnt += 1
                dfs(cnt)
                cnt -= 1
                board[i][j] = 0
result = 0
dfs(0)
print(result)
