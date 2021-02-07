# 0: 오른쪽이동, 1:위쪽이동, 2:왼쪽이동, 3:아래쪽이동
dx = [0,-1,0,1]
dy = [1,0,-1,0]

board = [[0]*(101) for _ in range(101)]
n = int(input())
for i in range(n):
    y,x,d,g = map(int,input().split())
    board[x][y] = 1 
    q = [d] # 현재 방향 
    temp = [d] # 축적된 방향
    for _ in range(g+1):
        for k in q:
            x += dx[k] # x,y는 계속 바뀌면서 움직여야 함
            y += dy[k]
            board[x][y] = 1
        # 0세대 //1세대  //2세대     //3세대 ...    
        # 0     //0,1    //0,1,2,1  //0,1,2,1,2,3,2,1 //...           
        # 전세대 +1 한 것의 뒤집어서 붙여나가 짐
        q = [(i+1)%4 for i in temp] # 오른쪽으로 회전(1증가 후 나머지 처리연산)
        q.reverse() # 뒤집기    
        temp += q # 축적방향에 추가
result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
            result +=1
print(result)
