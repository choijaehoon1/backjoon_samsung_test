import sys

def move_block(t,x,y):
    if t == 1:
        blue_board[x][0] = 1
        green_board[0][y] = 1
        
        index = 1
        while index < 6 and blue_board[x][index] == 0:
            blue_board[x][index-1] = 0
            blue_board[x][index] = 1
            index += 1

        index = 1
        while index < 6 and green_board[index][y] == 0:
            green_board[index-1][y] = 0
            green_board[index][y] = 1
            index += 1

    elif t == 2:
        blue_board[x][0] = 1
        blue_board[x][1] = 1
        green_board[0][y] = 1
        green_board[0][y+1] = 1

        index = 2
        while index < 6 and blue_board[x][index] == 0:
            blue_board[x][index-2] = 0
            blue_board[x][index] = 1
            index += 1

        index = 1
        while index < 6 and green_board[index][y] == 0 and green_board[index][y+1] == 0:
            green_board[index-1][y] = 0
            green_board[index-1][y+1] = 0
            green_board[index][y] = 1
            green_board[index][y+1] = 1
            index += 1

    elif t == 3:        
        blue_board[x][0] = 1
        blue_board[x+1][0] = 1
        green_board[0][y] = 1
        green_board[1][y] = 1

        index = 1
        while index < 6 and blue_board[x][index] == 0 and blue_board[x+1][index] == 0:
            blue_board[x][index-1] = 0
            blue_board[x+1][index-1] = 0
            blue_board[x][index] = 1
            blue_board[x+1][index] = 1
            index += 1

        index = 2
        while index < 6 and green_board[index][y] == 0:
            green_board[index-2][y] = 0
            green_board[index][y] = 1
            index += 1

def get_score():
    global answer
    # green
    for i in range(5,1,-1):
        cnt = 0
        for j in range(4):
            if green_board[i][j] == 0:
                break
            else:
                cnt += 1
        if cnt == 4:
            answer += 1
            clean_green(i)
            i += 1                        

    # blue
    for i in range(5,1,-1):
        cnt = 0
        for j in range(4):
            if blue_board[j][i] == 0:
                break
            else:
                cnt += 1
        if cnt == 4:
            answer += 1
            clean_blue(i)
            i += 1
    
def clean_green(line):
    for i in range(line,0,-1):
        for j in range(4):
            green_board[i][j] = green_board[i-1][j]

def clean_blue(line):
    for j in range(line,0,-1):
        for i in range(4):
            blue_board[i][j] = blue_board[i][j-1]

def check_green():
    cnt = 0
    for i in range(2):
        for j in range(4):
            if green_board[i][j] == 1:
                cnt += 1
                break              
    return cnt

def check_blue():
    cnt = 0
    for i in range(2):
        for j in range(4):
            if blue_board[j][i] == 1:
                cnt += 1
                break
    return cnt

def push_green(cnt):
    for i in range(5,1,-1):
        for j in range(4):
            green_board[i][j] = green_board[i-cnt][j]

    for i in range(2):
        for j in range(4):
            green_board[i][j] = 0

def push_blue(cnt):
    for i in range(5,1,-1):
        for j in range(4):
            blue_board[j][i] = blue_board[j][i-cnt]
    
    for i in range(2):
        for j in range(4):
            blue_board[j][i] = 0

def get_sum():
    cnt = 0
    for i in range(4):
        for j in range(6):
            if blue_board[i][j] == 1:
                cnt += 1
            if green_board[j][i] == 1:
                cnt += 1
    return cnt
            
blue_board = [[0]*6 for _ in range(4)]
green_board = [[0]*4 for _ in range(6)]

answer = 0
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    t,x,y = map(int,sys.stdin.readline().rstrip().split())
    move_block(t,x,y)
    get_score()
    push_green(check_green())
    push_blue(check_blue())
    
print(answer)
print(get_sum())
