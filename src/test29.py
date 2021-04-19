import sys

answer = 0
def dfs(depth,num):
    global answer

    if depth == 10: 
        answer = max(answer,num)
        return

    for i in range(4): # 처음말부터 4개말 수행
        x,next_x,move = chess[i],chess[i],dice[depth] # x는 이동하는 칸이라 생각(x가 현재 시행중 인것)

        # 이동할 칸이 파란색칸이면 한칸 미리 이동시킴
        if x == 5 or x == 10 or x == 15:
            x = move_in[x]
            move -= 1 # 이동주사위 횟수 하나 감소
        # x에서 주사위 만큼 이동했을때 21이하면 외각을 도는 경우임
        if move + x <= 21: # 한번에 이동
            x += move
        else:
            for _ in range(move): # 한칸씩 이동하며 값 갱신
                x = position[x]

        if visit[x] == 1 and x != 21: # 이동하는 칸이 마지막이 아닌데 방문한거면 무시
            continue

        visit[next_x],visit[x],chess[i] = 0,1,x # i번째 chess에 현재 이동한 칸 값 저장 후 방문처리
        dfs(depth+1,num + board[x]) # 이동한 칸의 board값 더해주고 재귀           
        visit[next_x],visit[x],chess[i] = 1,0,next_x # 원복

# 주사위 정보
dice = list(map(int,sys.stdin.readline().rstrip().split()))

position = [0 for _ in range(33)] # 시작 끝 포함총 33칸
# position은 다음칸에 대한 인덱스
for i in range(21):
    position[i] = i+1 # ex)인덱스 0번째는 첫번째 인덱스를 가리킨다
position[21] = 21 # 도착은 다음 인덱스 없게 멤돌게 함 21로 설정
position[22],position[23],position[24] = 23,24,30 # 24번 다음은 30번(10에서 오른쪽방향)
position[25],position[26] = 26,30 # 26다음은 30 (20에서 위쪽방향)
position[27],position[28],position[29] = 28,29,30 # 29 다음은 30을 보고 다른 값들(24,26)을 30으로 갱신 시킨것임(30에서 오른쪽 방향)
position[30],position[31],position[32] = 31,32,20 # 32번은 20번 인데그 가리킴

# board의 처음값과 마지막값은 0이므로 디폴트 설정 그대로 둠
board = [0 for _ in range(33)]
for i in range(1,21):
    board[i] = i*2
board[22],board[23],board[24] = 13,16,19
board[25],board[26] = 22,24
board[27],board[28],board[29] = 28,27,26
board[30],board[31],board[32] = 25,30,35

# 파란색으로 들어가는 경우
move_in = [0 for _ in range(16)]
move_in[5],move_in[10],move_in[15] = 22,25,27 # position의 인덱스로 설정(22,25,27)

chess = [0 for _ in range(4)] # 체스말
visit = [0 for _ in range(33)] # 같이 있는 것 체크용
dfs(0,0)
print(answer)

