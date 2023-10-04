import sys
from collections import deque
read = sys.stdin.readline



def bfs(i, j):
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [1 ,1, 1, 0, -1, -1, -1, 0]
    fill[i][j] = 0
    queue = deque()
    queue.append([i,j])

    while queue:
        b, a = queue.popleft()
        # fill[b][a] = 0
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if (0 <= x < w) and (0 <= y < h) and fill[y][x] == 1:
                fill[y][x] = 0 
                queue.append([y, x])





while True:
    w, h = map(int,read().split())
    if(w == 0 and h == 0): break
    cnt = 0
    fill = []
    for _ in range(h):
        fill.append(list(map(int,read().split())))
    
    for i in range(h):
        for j in range(w):
            if fill[i][j] == 1:
                bfs(i,j)
                cnt += 1

                
    print(cnt)



        
