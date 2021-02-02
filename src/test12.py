import sys
board = []
board.append(list(map(int,sys.stdin.readline().rstrip())))
board.append(list(map(int,sys.stdin.readline().rstrip())))
board.append(list(map(int,sys.stdin.readline().rstrip())))
board.append(list(map(int,sys.stdin.readline().rstrip())))

def rotate(n,d):
    rotate_list = [False for _ in range(4)]
    direction_list = [0 for _ in range(4)]
    rotate_list[n] = True # 회전해야함
    direction_list[n] = d # 왼쪽,오른쪽 저장해 둠
    # n은 검사 한것임
    tmp_n = n # 현재 번호
    tmp_d = d # 현재 방향
    for i in range(n+1,4): # n+1번째부터 검사
        if board[tmp_n][2] != board[i][6]:
            rotate_list[i] = True
            tmp_d = -tmp_d
            direction_list[i] = tmp_d
            tmp_n = i
        else: # 같으면 더이상 검사할 필요 x
            break

    tmp_n = n # 현재 번호
    tmp_d = d # 현재 방향
    for i in range(n-1,-1,-1): # n-1부터 검사 왼쪽 검사
        if board[tmp_n][6] != board[i][2]:
            rotate_list[i] = True
            tmp_d = -tmp_d
            direction_list[i] = tmp_d
            tmp_n = i
        else:
            break
    
    for i in range(len(rotate_list)):
        if rotate_list[i] == True:
            if direction_list[i] == 1: # 오른쪽으로 회전
                a = board[i].pop()
                board[i] = [a] + board[i]
            else: # 왼쪽으로 회전
                a = board[i].pop(0)
                board[i].append(a)

k = int(input())
for i in range(k):
    num,d = map(int,sys.stdin.readline().rstrip().split())
    rotate(num-1,d)

answer = 0
for i in range(4):
    if board[i][0] == 1:
        answer += 2**i
print(answer)        
