from collections import deque
import copy
import sys

def turn(array,d,k):
    q = deque()
    for i in array:
        q.append(i)

    if d == 0: # 시게
        for i in range(k):
            tmp = q.pop()
            q.appendleft(tmp)
    else: # 반시계      
        for i in range(k):
            tmp = q.popleft()
            q.append(tmp)
    array = list(q)
    return array

def check():
    flag = False
    # 수행하다보면 값이 board 값이 바뀌므로 check함수 수행할때 들어오는 board를 복사해서 사용해야 함
    tmp_board = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if tmp_board[i][0] != 0:
                if tmp_board[i][0] == board[i][1]:
                    board[i][0] = 0
                    board[i][1] = 0
                    flag = True
                if tmp_board[i][0] == board[i][m-1]:                
                    board[i][0] = 0
                    board[i][m-1] = 0
                    flag = True
            if tmp_board[i][m-1] != 0:                    
                if tmp_board[i][m-1] == board[i][m-2]:
                    board[i][m-1] = 0
                    board[i][m-2] = 0
                    flag = True
                if tmp_board[i][m-1] == board[i][0]:
                    board[i][m-1] = 0
                    board[i][0] = 0
                    flag = True

            if 1 <= j <= m-2:
                if tmp_board[i][j] != 0:
                    if tmp_board[i][j] == board[i][j-1]:
                        board[i][j] = 0
                        board[i][j-1] = 0
                        flag = True
                    if tmp_board[i][j] == board[i][j+1]:   
                        board[i][j] = 0
                        board[i][j+1] = 0
                        flag = True

            if tmp_board[0][j] != 0:
                if tmp_board[0][j] == board[1][j]:
                    board[0][j] = 0
                    board[1][j] = 0
                    flag = True
            if tmp_board[n-1][j] != 0:                    
                if tmp_board[n-1][j] == board[n-2][j]:
                    board[n-1][j] = 0
                    board[n-2][j] = 0                                
                    flag = True

            if 1 <= i <= n-2:
                if tmp_board[i][j] != 0:
                    if tmp_board[i][j] == board[i-1][j]:
                        board[i][j] = 0
                        board[i-1][j] = 0
                        flag = True
                    if tmp_board[i][j] == board[i+1][j]:   
                        board[i][j] = 0
                        board[i+1][j] = 0
                        flag = True
    return flag    

board = []
n,m,t = map(int,sys.stdin.readline().rstrip().split())
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))                    

for i in range(t):
    x,d,k = map(int,input().split())
    for j in range(x-1,n,x):
        board[j] = turn(board[j],d,k)
    # print(board)
    flag = check() # board 갱신, flag
    if flag == False:
        tmp = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] != 0:
                    cnt += 1
                    tmp += board[i][j]
        if cnt != 0: # cnt가 0일때는 런타임에러 되므로                   
            avg = tmp / cnt               
            for i in range(n):
                for j in range(m):
                    if board[i][j] != 0:
                        if board[i][j] > avg:
                            board[i][j] -=1
                        elif board[i][j] < avg:
                            board[i][j] +=1                    

answer = 0
for i in range(n):
    answer += sum(board[i])
print(answer)    

