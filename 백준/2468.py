import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(a,b,h):
    queue = deque()
    queue.append([a,b])
    visit[a][b] = 1
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < n and 0 <= xx < n and visit[yy][xx] == 0 and graph[yy][xx] > h:
                visit[yy][xx] = 1
                queue.append([yy,xx])

    return 1


n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

result = 100
maxre = 0
he = 0
while result > 0:
    result = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > he and visit[i][j] == 0:
                result += bfs(i,j,he)
    maxre = max(maxre, result)
    he += 1

print(maxre)