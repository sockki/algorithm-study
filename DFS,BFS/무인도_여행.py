from collections import deque

def solution(maps):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    w = len(maps[0])
    h = len(maps)
    answer = []
    visit = [[0 for i in range(w)] for i in range(h)]
            
    def bfs(a,b,c):
        nonlocal visit, answer
        queue = deque()
        queue.append([a,b])
        visit[a][b] = 1
        result = int(c)
        while queue:
            y,x = queue.popleft()
            for i in range(4):
                yy = y + dy[i]
                xx = x + dx[i]
                if 0<=yy<h and 0<=xx<w and not visit[yy][xx] and maps[yy][xx] != "X":
                    result += int(maps[yy][xx])
                    visit[yy][xx] = 1
                    queue.append([yy,xx])
        
        answer.append(result)
            
    for i in range(h):
        for j in range(w):
            if maps[i][j] != "X" and not visit[i][j]:
                bfs(i,j,maps[i][j])
    
    if not answer:
        answer.append(-1)
    answer.sort()
    
    return answer