from collections import deque
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(n):
        if board[i][j] == 9:
            start_x,start_y = i,j
            board[i][j] = 0

# 먹을 수 있는 물고기 찾고 최단거리도 구해서 리턴
def check(x,y):
    q = deque()
    visit[x][y] = 1
    q.append([x,y])
    check_list = []
    dist = [[-1]*n for _ in range(n)]
    dist[x][y] = 0

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x +dx[k]
            ny = y +dy[k]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
                if board[nx][ny] <= start_size or board[nx][ny] == 0:
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
                if board[nx][ny] < start_size and board[nx][ny] != 0:
                    check_list.append([nx,ny,dist[nx][ny]])
    check_list.sort(key=lambda x:(x[2],x[0],x[1])) # 최단거리 가장 짧은거 찾고 그중 제일위,제일왼쪽순 정렬       
    return check_list
answer = 0
ate = 0
start_size = 2
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while True:
    visit = [[0]*n for _ in range(n)]
    result = check(start_x,start_y)
    if result == []:
        print(answer)
        break
   
    x,y,min_value = result[0]
    answer += min_value    
    start_x,start_y = x,y
    board[x][y] = 0   
    ate += 1

    if ate >= start_size:
        ate = 0        
        start_size += 1
