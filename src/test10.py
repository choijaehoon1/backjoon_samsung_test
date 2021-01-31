from itertools import combinations
import sys
n = int(sys.stdin.readline().rstrip())
data = [i for i in range(n)]
total = list(combinations(data,n//2))

board = []
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))

start = []
link = []
for i in range(len(total)//2):
    start.append(total[i])
    link.append(total[i+len(total)//2])

answer = 1e9

for i in range(len(start)):
    j = (len(start)-1) - i
    start_num = 0
    link_num = 0
    for x in range(len(start[i])):
        for y in range(x+1,len(start[i])):
            start_num += board[start[i][x]][start[i][y]] + board[start[i][y]][start[i][x]]
            link_num  += board[link[j][x]][link[j][y]] + board[link[j][y]][link[j][x]]
    answer = min(answer,abs(start_num-link_num))            
print(answer)


