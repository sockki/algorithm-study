import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    day = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                queue.append([i,j,0])
    
    while queue:
        y, x, d = queue.popleft()
        for a in range(4):
            xx = x + dx[a]
            yy = y + dy[a]
            if(0<= xx < m and 0<= yy < n and field[yy][xx] == 0):
                queue.append([yy, xx, d+1])
                field[yy][xx] = 1
                day = d + 1
    return day
                
    
    



m, n = map(int, sys.stdin.readline().split())
field = []
for _ in range(n):
    field.append(list(map(int,sys.stdin.readline().split())))

result = bfs()

next = False
for i in field:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
print(result)