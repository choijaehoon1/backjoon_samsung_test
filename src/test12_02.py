import sys
from collections import deque
board = []
board.append(list(map(int,sys.stdin.readline().rstrip())))
board.append(list(map(int,sys.stdin.readline().rstrip())))
board.append(list(map(int,sys.stdin.readline().rstrip())))
board.append(list(map(int,sys.stdin.readline().rstrip())))

q = deque()
for i in board:
    q.append(deque(i))

def right(n,d):
    if n > 3 or q[n-1][2] == q[n][6]: # 범위 벗어나거나 값이 같은경우 종료
        return
    if q[n-1][2] != q[n][6]:
        right(n+1,-d) # 극이 다르면 반대방향으로 수행 됨
        q[n].rotate(d) # 1이면 시계방향, -1이면 반시계

def left(n,d):
    if n < 0 or q[n+1][6] == q[n][2]: # 범위 벗어나거나 값이 같은경우 종료
        return
    if q[n+1][6] != q[n][2]:
        left(n-1,-d) # 극이 다르면 반대방향으로 수행 됨
        q[n].rotate(d) # 1이면 시계방향, -1이면 반시계


k = int(sys.stdin.readline().rstrip())
for i in range(k):
    num,d = map(int,sys.stdin.readline().rstrip().split()) # 현재 회전 정보
    check_num = num - 1 # 인덱스 맞추기
    # 기준과는 반대방향으로 회전하고 각각 오른쪽 왼쪽 확인(오른쪽,왼쪽함수에서 먼저 rotate 수행됨)
    # 조건대로 현재 방향과 반대방향으로 수행됨
    right(check_num+1,-d)
    left(check_num-1,-d)
    # 제시된 조건대로 현재 것을 마지막에 rotate해야 주어진 조건 만족
    q[check_num].rotate(d)

answer = 0
for i in range(4):
    answer += (2**i) * q[i][0]
print(answer)        
