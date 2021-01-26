# 제일 위의 행부터 시작하여 아래행들을 탐색
def move_up(board):
    for i in range(n): # 열에 대해서 행을 검사
        p = 0 # 시작행
        x = 0 # 이전 블럭 초기값
        for j in range(n): # 행
            if board[j][i] == 0: # 빈칸이면 이동시킬 필요 없음
                continue 
            if x == 0: # 이전 블럭값이 빈칸이면 값을 현재 탐색하는 값으로 갱신
                x = board[j][i]
            else: # 이전 블럭값이 있으면                
                if x == board[j][i]: # 값이 같으면
                    board[p][i] = x*2 # 현재에서 파악한 제일 위의 값 갱신
                    x = 0 # 더했으니 0처리
                    p += 1 # 가장 위쪽 채웠으니 행증가시켜 아래쪽 검사
                else: # 값이 다른 경우
                    board[p][i] = x # 현재에서 파악한 제일 위의 값 갱신
                    x = board[j][i] # 값이 다르므로 이전블럭값 갱신
                    p += 1 # 가장 위쪽 채웠으니 행증가시켜 아래쪽 검사
            board[j][i] = 0 # 현재 탐색한 블록은 이동하였므로 0으로 갱신
        if x != 0: # 마지막 행까지 내려왔는데 이전 블럭값이 0이 빈칸이 아니면
            board[p][i] = x # ex) else문에 걸려 이전 블럭의 값이 넣어지고 행이 증가한 경우임
    return board

# 제일 아래 행부터 시작하여 위행들을 계속 탐색
def move_down(board):
    for i in range(n): # 열에 대해서 행을 검사
        p = n-1 # 시작 행
        x = 0 # 이전 블럭 초기값
        for j in range(n-1,-1,-1): # 행
            if board[j][i] == 0: # 빈칸이면 이동시킬 필요 없음
                continue 
            if x == 0: # 이전 블럭값이 빈칸이면 값을 현재 탐색하는 값으로 갱신
                x = board[j][i]
            else: # 이전 블럭값이 있으면                
                if x == board[j][i]: # 값이 같으면
                    board[p][i] = x*2 # 현재에서 파악한 제일 아래의 값 갱신
                    x = 0 # 더했으니 0처리
                    p -= 1 # 행 감소
                else: # 값이 다른 경우
                    board[p][i] = x # 현재에서 파악한 제일 아래의 값 갱신
                    x = board[j][i] # 값이 다르므로 이전블럭값 갱신
                    p -= 1 # 행 감소
            board[j][i] = 0 # 현재 탐색한 블록은 이동하였므로 0으로 갱신
        if x != 0: # 첫번째 행까지 올라왔는데 이전 블럭값이 0이 빈칸이 아니면
            board[p][i] = x # ex) else문에 걸려 이전 블럭의 값이 넣어지고 행이 감소한 경우임
    return board

# 제일 오른쪽 열부터 시작하여 왼쪽 열들을 탐색
def move_right(board):
    for i in range(n): # 행에 대해서 열을 검사
        p = n-1 # 시작 열
        x = 0 # 이전 블럭 초기값
        for j in range(n-1,-1,-1): # 행
            if board[i][j] == 0: # 빈칸이면 이동시킬 필요 없음
                continue 
            if x == 0: # 이전 블럭값이 빈칸이면 값을 현재 탐색하는 값으로 갱신
                x = board[i][j]
            else: # 이전 블럭값이 있으면                
                if x == board[i][j]: # 값이 같으면
                    board[i][p] = x*2 # 현재에서 파악한 제일 오른쪽의 값 갱신
                    x = 0 # 더했으니 0처리
                    p -= 1 # 가장 오른쪽은 채웠으니 열 감소시켜 탐색
                else: # 값이 다른 경우
                    board[i][p] = x # 현재에서 파악한 제일 오른쪽의 값 갱신
                    x = board[i][j] # 값이 다르므로 이전블럭값 갱신
                    p -= 1 # 가장 오른쪽은 채웠으니 열 감소시켜 탐색
            board[i][j] = 0 # 현재 탐색한 블록은 이동하였므로 0으로 갱신
        if x != 0: # 첫번째 행까지 올라왔는데 이전 블럭값이 0이 빈칸이 아니면
            board[i][p] = x # ex) else문에 걸려 이전 블럭의 값이 넣어지고 열이 감소한 경우임
    return board

# 제일 왼쪽 열부터 시작하여 오른쪽 열들을 탐색
def move_left(board):
    for i in range(n): # 행에 대해서 열을 검사
        p = 0 # 시작 열
        x = 0 # 이전 블럭 초기값
        for j in range(n): # 행
            if board[i][j] == 0: # 빈칸이면 이동시킬 필요 없음
                continue 
            if x == 0: # 이전 블럭값이 빈칸이면 값을 현재 탐색하는 값으로 갱신
                x = board[i][j]
            else: # 이전 블럭값이 있으면                
                if x == board[i][j]: # 값이 같으면
                    board[i][p] = x*2 # 현재에서 파악한 제일 왼쪽 값 갱신
                    x = 0 # 더했으니 0처리
                    p += 1 # 열 증가
                else: # 값이 다른 경우
                    board[i][p] = x # 현재에서 파악한 제일 오른쪽의 값 갱신
                    x = board[i][j] # 값이 다르므로 이전블럭값 갱신
                    p += 1 # 열 증가
            board[i][j] = 0 # 현재 탐색한 블록은 이동하였므로 0으로 갱신
        if x != 0: # 첫번째 행까지 올라왔는데 이전 블럭값이 0이 빈칸이 아니면
            board[i][p] = x # ex) else문에 걸려 이전 블럭의 값이 넣어지고 열이 증가한 경우임
    return board

def dfs(tmp_board,cnt):
    global answer
    if cnt == 5:
        for i in range(n):
            answer = max(answer, max(tmp_board[i]))
        return

    # 재귀함수로 들어갈때마다 배열을 카피해줘야 한다
    dfs(move_up(copy.deepcopy(tmp_board)), cnt+1)
    dfs(move_down(copy.deepcopy(tmp_board)), cnt+1)
    dfs(move_left(copy.deepcopy(tmp_board)), cnt+1)
    dfs(move_right(copy.deepcopy(tmp_board)), cnt+1)

import copy
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

answer = 0
dfs(board,0)
print(answer)

