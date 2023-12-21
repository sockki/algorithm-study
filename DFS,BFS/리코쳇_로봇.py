from collections import deque

def solution(board):
    answer = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    w = len(board[0])
    h = len(board)
    visit = [[999999 for _ in range(w)] for _ in range(h)]
    queue = deque()
    for i in range(h):
        for j in range(w):
            if board[i][j] == "R":
                visit[i][j] = 0
                queue.append([i,j,0])
        if queue:
            break
    
    while queue:
        y,x,c = queue.popleft()
        
        if board[y][x] == "G":
            return c
        
        for i in range(4):
            xx = x
            yy = y
            while 0<=yy + dy[i]<h and 0<=xx + dx[i]< w and board[yy + dy[i]][xx + dx[i]] != "D":
                xx += dx[i]
                yy += dy[i]
                
            if visit[yy][xx] > c + 1:
                visit[yy][xx] = c + 1
                queue.append([yy,xx,c+1])
                

    return -1