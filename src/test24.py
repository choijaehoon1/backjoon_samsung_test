from collections import Counter
import copy

def process():
    max_len = 0 
    row = len(board)
    for i in range(row): # 각 행에 대해
        check = [j for j in board[i] if j != 0] # 0은 카운트 제외
        check_list = Counter(check).most_common()
        check_list.sort(key=lambda x:(x[1],x[0])) # 주어진 조건대로 정렬
        board[i] = [] # 각 행의 원소넣는 리스트
        for num,cnt in check_list:
            board[i].append(num)
            board[i].append(cnt)

        c_len = len(check_list) # 현재 길이(c_len은 2가지 원소가 있는 튜플형태가 하나로 취급되므로 최대길이는 *2)
        if max_len < c_len*2: # 최대길이 갱신
            max_len = c_len*2
    for i in range(row):
        for j in range(max_len-len(board[i])): # 각행이 최대길이 보다 짧은 경우 0 추가
            board[i].append(0)
        board[i] = board[i][:100] # 100보다 길어지면 자르기

r,c,k = map(int,input().split())
board = []
for i in range(3):
    board.append(list(map(int,input().split())))

time = 0
while True:
    if time > 100:
        print(-1)
        break
    try:
        if board[r-1][c-1] == k:
            print(time)
            break
    except:
        pass
    row = len(board)        
    column = len(board[0])
    if row < column: # C연산
        # 2차원배열인 board에 *로 언패킹하고 zip연산을 통해 
        # 각 행의 첫번째원소들, 두번째원소들 ... 묶어서 -> 리스트 형태로 변환
        # 즉 2차원리스트 회전
        board = list(zip(*board)) # 열이 행이 됨 (트랜스포즈)
        process() # 행처럼 처리
        board = list(zip(*board)) # 행처럼 처리했으므로 다시 원래형태로 만들어야 함  (트랜스포즈)
    else: # R연산
        process() # 행처리        

    time += 1        

