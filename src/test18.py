from collections import deque
n,l,r = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(x,y):
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    possible = []
    possible.append([x,y])
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    possible.append([nx,ny])
                    visit[nx][ny] = 1
                    q.append([nx,ny])
    return possible

def bfs(array):
    s = 0
    cnt = 0
    for x,y in array:
        s += board[x][y]
        cnt += 1
    num = s//cnt
    for x,y in array:
        board[x][y] = num

answer = 0
while True:
    visit = [[0]*n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                tmp_list = check(i,j)
                if len(tmp_list) > 1:
                    flag = True
                    bfs(tmp_list)
    if flag == False:
        break
    answer += 1
print(answer)


