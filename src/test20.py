from collections import deque
import sys
n,m,k = map(int,sys.stdin.readline().rstrip().split())
sail = [[5]*n for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]

winter = []
for i in range(n):
    winter.append(list(map(int,sys.stdin.readline().rstrip().split())))

for i in range(m):
    x,y,z = map(int,sys.stdin.readline().rstrip().split())
    tree[x-1][y-1].append(z)

def spring():
    summer = [] # 여름 처리
    for i in range(n):
        for j in range(n):
            length = len(tree[i][j]) # 나무가 있을때만 반복
            for k in range(length):
                # 나무가 양분을 먹을 수 있을 때
                if tree[i][j][k] <= sail[i][j]:
                    sail[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1 # 나이 1 증가
                else: # 양분 못먹을 때는 k번째부터 뒤에서부터 pop해줘야 함
                    for _ in range(k,length): # k이전까지는 양분먹을 수 있으므로 k부터 끝까지 확인
                        tmp = tree[i][j].pop() # 하나씩 뒤에서 빼 줌
                        summer.append((i,j,tmp//2)) # 죽은나무 여름에 처리해주는 리스트에 값 저장
                    break
    # 여름에 양분 추가
    for x,y,t in summer:
        sail[x][y] += t

# 8방향
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def fall():
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) != 0: # 양분이 있을때만 확인
                for k in range(len(tree[i][j])):
                    if tree[i][j][k] % 5 == 0: # 5의 배수이면 8방향에 1증가
                        for z in range(8):
                            nx = dx[z] + i
                            ny = dy[z] + j
                            if 0<=nx<n and 0<=ny<n:
                                tree[nx][ny].appendleft(1) # appendleft 어린 나무부터 양분 먹기 위해

    for i in range(n):
        for j in range(n):
            sail[i][j] += winter[i][j]

for i in range(k):
    spring()
    fall()

cnt = 0
for i in range(n):
    for j in range(n):
        if tree[i][j] != 0:
            cnt += len(tree[i][j])
print(cnt)
