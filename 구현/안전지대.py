def solution(board):
    answer = 0
    visit = [[0 for _ in range(len(board[0]))] for _ in range(len(board[0]))]
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]
    def discount(y,x):
        visit[y][x] = 1
            
        for i in range(8):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < len(board[0]) and 0 <= xx < len(board[0]) and visit[yy][xx] == 0:
                visit[yy][xx] = 1
                
    
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                discount(i,j)
        
    for i in visit:
        answer += i.count(0)
    return answer