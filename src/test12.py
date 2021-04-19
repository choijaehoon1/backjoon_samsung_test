import sys
n,l = map(int,sys.stdin.readline().rstrip().split())

board = []
check_list = []
for i in range(n):
    data = list(map(int,sys.stdin.readline().rstrip().split()))
    board.append(data)
    check_list.append(data)

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(board[j][i])
    check_list.append(tmp)

def get_possible(array):
    visit = [False for _ in range(n)] # 방문처리 용도
    for i in range(len(array)-1):
        if array[i] == array[i+1]: # 값이 같으면 패스
            continue
        if abs(array[i]-array[i+1]) > 1: # 높이 1보다 크게 차이나면 불가능
            return False
        # 앞의 값이 큰 경우
        if array[i] > array[i+1]:
            tmp_height = array[i+1] # 경사로 높이(현재 케이스는 앞의 값이 큰 경우이므로 뒤의 값 저장)
            for j in range(i+1,i+1+l): # l길이 만큼 뒷부분이 연결되어 있는지 확인
                if 0<=j<n: # 범위 안에 있는데
                    if array[j] != tmp_height: # 높이가 다르면 false
                        return False
                    if visit[j] == True: # 이미 방문했으면 return False
                        return False
                    visit[j] = True # 방문처리
                else:
                    return False                                                            
        # 뒤의 값이 큰 경우                    
        elif array[i] < array[i+1]:
            tmp_height = array[i] # 경사로 높이(현재 케이스는 뒤의 값이 큰 경우이므로 앞의 값 저장)
            for j in range(i,i-l,-1): # l길이 만큼 앞부분이 연결되어 있는지 확인 
                if 0<=j<n: # 범위 안에 있는데
                    if array[j] != tmp_height: # 높이가 다르면 false
                        return False
                    if visit[j] == True: # 이미 방문했으면 return False
                        return False
                    visit[j] = True # 방문처리
                else:
                    return False                                                            
    return True

answer = 0
for check in check_list:
    if get_possible(check): # true
        answer += 1
print(answer)
